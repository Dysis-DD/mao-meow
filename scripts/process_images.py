# -*- coding: utf-8 -*-
"""
Mao.MEOW Image Batch Processor
Compress and resize source images for web use
Output: images/ folder
"""
from PIL import Image
import os
import sys

# Force UTF-8 output on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "预设图片")
OUT_DIR = os.path.join(BASE_DIR, "images")

os.makedirs(OUT_DIR, exist_ok=True)

IMAGES = [
    {
        "src": "mao品牌logo.png",
        "out": "logo-neon.png",
        "size": (512, 512),
        "fmt": "PNG",
        "max_colors": 256,
    },
    {
        "src": "KO-证件照.png",
        "out": "ko-id.jpg",
        "size": (600, 600),
        "fmt": "JPEG",
        "quality": 85,
    },
    {
        "src": "花花-证件照.png",
        "out": "huahua-id.jpg",
        "size": (600, 630),
        "fmt": "JPEG",
        "quality": 85,
    },
    {
        "src": "铲屎官图片.png",
        "out": "d-id.jpg",
        "size": (600, 600),
        "fmt": "JPEG",
        "quality": 85,
    },
    {
        "src": "产品-喵感耳机.png",
        "out": "product-meowsense.png",
        "size": (400, 533),
        "fmt": "PNG",
        "max_colors": 256,
    },
    {
        "src": "产品-胡须导航仪.png",
        "out": "product-whiskernav.png",
        "size": (400, 533),
        "fmt": "PNG",
        "max_colors": 256,
    },
    {
        "src": "产品-桌面空间重组系统.png",
        "out": "product-dsd.png",
        "size": (600, 338),
        "fmt": "PNG",
        "max_colors": 256,
    },
    {
        "src": "产品-协同编程助手.png",
        "out": "product-maocode.png",
        "size": (400, 533),
        "fmt": "PNG",
        "max_colors": 256,
    },
    {
        "src": "鼠标-图标.png",
        "out": "cursor-paw.png",
        "size": (64, 64),
        "fmt": "PNG",
        "max_colors": 64,
    },
]


def process_image(cfg):
    """Process a single image"""
    src_path = os.path.join(SRC_DIR, cfg["src"])
    out_path = os.path.join(OUT_DIR, cfg["out"])

    if not os.path.exists(src_path):
        print(f"  [FAIL] Source not found: {cfg['src']}")
        return None

    im = Image.open(src_path)
    original_size = im.size
    original_mode = im.mode

    # Convert RGBA to RGB for JPEG output
    if cfg["fmt"] == "JPEG" and im.mode in ("RGBA", "P"):
        if im.mode == "RGBA":
            bg = Image.new("RGB", im.size, (10, 10, 26))
            bg.paste(im, mask=im.split()[3])
            im = bg
        else:
            im = im.convert("RGB")
    elif cfg["fmt"] == "PNG" and im.mode == "RGBA":
        pass
    elif im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA")

    # Resize with aspect ratio preserved
    im.thumbnail(cfg["size"], Image.LANCZOS)

    # Save
    save_kwargs = {"optimize": True}
    if cfg["fmt"] == "JPEG":
        save_kwargs["quality"] = cfg.get("quality", 85)
    elif cfg["fmt"] == "PNG" and "max_colors" in cfg:
        if im.mode == "RGBA":
            # FASTOCTREE (method=2) supports RGBA, MEDIANCUT does not
            im = im.quantize(colors=cfg["max_colors"], method=Image.Quantize.FASTOCTREE)
        else:
            im = im.convert("RGB").quantize(colors=cfg["max_colors"], method=Image.Quantize.MEDIANCUT)

    im.save(out_path, format=cfg["fmt"], **save_kwargs)

    out_size = os.path.getsize(out_path)
    print(f"  [OK] {cfg['src']}")
    print(f"     {original_size[0]}x{original_size[1]} ({original_mode})"
          f" -> {im.size[0]}x{im.size[1]} ({cfg['fmt']})"
          f" -> {out_size/1024:.1f} KB")

    return out_size


def main():
    print("=" * 60)
    print("Mao.MEOW Image Processor")
    print(f"Source: {SRC_DIR}")
    print(f"Output: {OUT_DIR}")
    print("=" * 60)

    total_size = 0
    success = 0
    fail = 0

    for cfg in IMAGES:
        size = process_image(cfg)
        if size:
            total_size += size
            success += 1
        else:
            fail += 1

    print("=" * 60)
    print(f"Result: {success} success / {fail} fail")
    print(f"Total size: {total_size/1024:.1f} KB ({total_size/1024/1024:.2f} MB)")
    target_mb = 2.0
    if total_size/1024/1024 < target_mb:
        print(f"[OK] Total < {target_mb}MB, passed!")
    else:
        print(f"[WARN] Total exceeds {target_mb}MB, needs optimization")
    print("=" * 60)


if __name__ == "__main__":
    main()
