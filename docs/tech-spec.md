# Mao.MEOW 技术规范

---

## 技术选型

| 层面 | 选择 | 说明 |
|------|------|------|
| 框架 | 无（纯 HTML/CSS/JS） | 零依赖，双击打开 |
| 动画引擎 | Canvas（进入动画）+ CSS transition/animation | Canvas 做复杂序列，CSS 做页面动效 |
| 滚动检测 | IntersectionObserver API | 原生、高性能、无 scroll 监听器 |
| 横向滚动 | CSS scroll-snap | 原生支持 Chrome/Edge/Firefox |
| 图片处理 | Python Pillow（一次性脚本） | 离线压缩后输出到 images/ |
| 部署 | 本地文件 `file://` 协议 | 无服务器需求 |

---

## 浏览器支持
- **主要**：Chrome (latest)
- **次要**：Edge (Chromium)、Firefox (latest)
- **不要求**：Safari、IE

---

## 文件组织

```
MAO/
├── index.html              # 主文件（HTML+CSS+JS 内嵌）
├── 404.html                # 独立 404 页面
├── CLAUDE.md               # AI 助手指引
├── docs/                   # 项目文档
├── devlog/                 # 开发日志
├── images/                 # 处理后图片（<= 2MB 总大小）
├── 预设图片/                # 原始素材（只读）
└── scripts/                # 工具脚本
    └── process_images.py   # 图片压缩
```

---

## CSS 设计令牌

### 配色
```css
:root {
  --bg-deep:           #050510;     /* 暗物质黑 */
  --bg-section:        #0a0a1a;     /* Section 底色 */
  --meow-cyan:         #00f0ff;     /* 喵青霓虹主色 */
  --meow-cyan-dim:     rgba(0,240,255,0.3);
  --meow-cyan-glow:    rgba(0,240,255,0.6);
  --terminal-green:    #00ff41;     /* 终端绿 */
  --purple-deep:       #1a0a2e;     /* 深空紫黑 */
  --purple-glow:       rgba(128,0,255,0.5);
  --text-primary:      #e0e0f0;
  --text-dim:          rgba(224,224,240,0.5);
  --card-bg:           rgba(10,10,30,0.7);
  --card-border:       rgba(0,240,255,0.15);
}
```

### 霓虹发光复用
```css
  --neon-glow-cyan:    0 0 7px var(--meow-cyan),
                        0 0 20px var(--meow-cyan-dim),
                        0 0 40px var(--meow-cyan-dim);
  --neon-glow-purple:  0 0 7px var(--purple-glow),
                        0 0 20px var(--purple-glow);
```

### 排版
```css
  --font-mono:    'Consolas', 'Courier New', monospace;
  --font-display: 'Segoe UI', 'Helvetica Neue', sans-serif;
  --font-cn:      'Microsoft YaHei', 'PingFang SC', sans-serif;
```

### 间距
```css
  --section-pad:  120px 5vw;
  --header-height: 64px;
```

### 动效时长
```css
  --t-fast:    0.2s;
  --t-normal:  0.4s;
  --t-slow:    0.8s;
  --t-glacial: 1.6s;
```

---

## 图片处理规格

| 图片 | 目标尺寸 | 目标格式 | 目标大小 |
|------|----------|----------|----------|
| 品牌 Logo | 512×512 | PNG-8 | < 150KB |
| KO 证件照 | 600×600 | JPEG q85 | < 80KB |
| 花花证件照 | 600×630 | JPEG q85 | < 80KB |
| 铲屎官图片 | 600×600 | JPEG q85 | < 80KB |
| 喵感耳机 | 400×533 | PNG-8 | < 100KB |
| 胡须导航仪 | 400×533 | PNG-8 | < 100KB |
| 桌面重组系统 | 600×338 | PNG-8 | < 100KB |
| 协同编程助手 | 400×533 | PNG-8 | < 100KB |
| 鼠标光标 | 32×32 / 64×64 | PNG-8 | < 5KB |
| **合计** | | | **< 800KB** |

---

## JS 模块架构（index.html 内）

```
CONFIG              — 全局常量（颜色、时间、粒子数等）
EntryAnimation      — Canvas 进入动画状态机
FloatingParticles   — 背景浮动光点
CustomCursor        — 自定义光标 + 发光拖尾
ScrollAnimations    — IntersectionObserver 入场揭示
EasterEgg           — 隐藏小鱼干 + 猫跑动画
WhitepaperModal     — 产品详情弹窗
ContactForm         — 联系表单 + Toast
FooterDanmaku       — 底部弹幕
```

模块间通信：通过 DOM 事件和 `data-*` 属性解耦。

---

## 性能指标
- 首次内容绘制 < 2 秒（本地文件）
- 图片总大小 < 1MB
- 无内存泄漏（粒子自动回收、Observer 断开）
- 动画使用 `transform` / `opacity` 实现 GPU 合成
- Canvas 使用逻辑分辨率（1x），2x/3x 屏接受略微模糊
