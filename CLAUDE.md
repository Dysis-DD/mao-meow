# Mao.MEOW — AI 助手项目指引

## 项目简介
为虚构猫咪科技公司 Mao.MEOW 创建赛博朋克风格的单页官网。用户为代码小白，所有操作需保持简单。

## 核心原则
- **分步推进**：每阶段产出可验证结果，不要一口气做太多
- **稳定安全**：每次只修改必要文件，改完验证再继续
- **保持简洁**：纯 HTML/CSS/JS，零依赖，零构建工具

---

## 标准文件路径

| 用途 | 路径 |
|------|------|
| 主网站 | `MAO官网.html` |
| 404 页面 | `404.html` |
| 需求文档 | `docs/requirements.md` |
| 技术规范 | `docs/tech-spec.md` |
| 设计规范 | `docs/design-standards.md` |
| 执行步骤 | `docs/execution-steps.md` |
| 开发日志 | `devlog/YYYY-MM-DD.md` |
| 图片处理脚本 | `scripts/process_images.py` |
| 处理后图片 | `images/` |
| 原始素材 | `预设图片/`（只读，勿修改） |
| 暂不使用素材 | `预设图片/暂存-不使用/`（忽略） |
| 实施计划 | Claude 内部 plan 文件 |

---

## 工作流程

### 每次开发会话
1. 查看 `docs/execution-steps.md` 确定当前阶段
2. 只做当前阶段的工作，不跨越阶段
3. 完成后更新执行步骤的勾选状态
4. 在 `devlog/` 创建或更新当日日志

### 开发日志格式
```markdown
# 开发日志 — YYYY-MM-DD

## 今日完成
- [x] 具体完成事项

## 待办事项
- [ ] 下一步要做的事

## 备注
任何需要注意的问题
```

### 验证要求
每阶段完成后必须：
1. 在浏览器打开 `index.html` 确认效果
2. 对照 `docs/execution-steps.md` 中该阶段的验证条目
3. 确认无问题后再进入下一阶段

---

## 设计速查

### 配色
- 暗物质黑 `#050510` | 喵青霓虹 `#00f0ff` | 终端绿 `#00ff41` | 深空紫黑 `#1a0a2e`

### 核心文案
- 主 Slogan："Wiring the purr into your heartbeat. / 把呼噜声，写进你的心跳里。"
- 副 Tagline："Powered by purrs. Approved by paws. / 呼噜供能，肉垫盖章。"

### 品牌名格式
- 正式：**Mao.MEOW**（首字母大写，中间有英文句点）
- 不要写成：mao meow / MaoMeow / mao.meow

---

## 注意事项
- 改动 `预设图片/` 里的原始文件前必须确认
- `预设图片/暂存-不使用/` 里的文件不纳入项目
- CSS 动画尽量用 `transform` 和 `opacity`（GPU 加速）
- JavaScript 用 IIFE 模块模式组织，避免全局变量污染
- 所有图片引用使用 `images/` 而非 `预设图片/`
