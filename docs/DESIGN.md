# OFF-DUTY TERMINAL

zlcwwhq 的 GitHub 个人主页视觉说明。

## 概念

**战术档案 × 雨夜咖啡馆。** 从明日方舟的工业氛围、档案编号与克制排版出发，以少女前线春田的亲切感、栗色头发和咖啡馆暖光作为视觉中心。

保留原主页的事实：斯图加特大学电气工程硕士在读；热爱编程；工具包括 C、C++、Go、Rust；正在探索 Vibe Coding。新增用户明确提供的爱好：明日方舟、少女前线与春田。页面没有虚构项目、技能评级、在线状态或统计数据。

## 视觉规范

| 用途 | 色值 |
| --- | --- |
| 墨蓝底色 | `#141e28` |
| 暖白文字 | `#eee7db` |
| 琥珀强调 | `#cf9e62` |
| 雾蓝强调 | `#90b5c8` |
| 次级文字 | `#a3adb5` |

- 主视觉使用衬线个人标识、等宽档案标记与冷暖光对照。
- 卡片使用切角、细线网格、原创几何图形；未复制游戏官方徽标。
- 正文使用 GitHub 原生文字，保留可选中、可搜索与自动换行的能力。
- 兴趣卡片使用固定最大展示宽度，窄屏可自然换行，不使用固定列数表格。
- 全部展示图片从本仓库加载；无需第三方徽章服务、动态统计服务、JavaScript 或定时工作流。
- 所有图片含替代文字，SVG 含标题与描述。SVG 不含脚本、外链资源或动画。

## 文件与维护

| 路径 | 用途 |
| --- | --- |
| `README.md` | 主页内容与链接 |
| `assets/springfield-terminal.webp` | 春田主视觉，1774 × 887；AI 生成插画的 WebP 展示版本 |
| `assets/open-repositories.svg` | 代码仓库入口 |
| `assets/lang-*.svg` | 技术徽章 |
| `assets/arknights-dossier.svg` | 明日方舟兴趣卡片 |
| `assets/gfl-dossier.svg` | 少女前线兴趣卡片 |
| `assets/terminal-footer.svg` | 结尾标记 |
| `scripts/build-assets.py` | 使用 Python 标准库重新生成 SVG |

运行 `python3 scripts/build-assets.py` 可重新生成全部矢量素材，适合调整文案与配色；不会修改春田主视觉。更新个人信息直接编辑 README，不需要运行构建工具。

## 素材来源

- [春田角色资料 / IOP Wiki](https://iopwiki.com/wiki/Springfield)：角色外观、服装与咖啡馆相关设定参考。
- [春田立绘参考页 / ドールズフロントライン Wiki](https://wikiwiki.jp/dolls-fl/スプリングフィールド)：本次生图使用的角色参考图来自该页的「別立ち絵」。参考图只用于角色识别，未作为主页素材直接分发。
- [明日方舟官方网站](https://ak.hypergryph.com/)：世界观与视觉氛围参考。
- [少女前线官方网站](https://gf.sunborngame.com/)：兴趣卡片链接。

角色与游戏相关知识产权属于各自权利人。主视觉是使用 ChatGPT 内置 imagegen 制作的 AI 生成同人插画，不是官方立绘，也不表示官方背书。其余矢量图形为本主页定制设计。

## 主视觉生成提示词

生成方式：ChatGPT 内置 imagegen；使用春田立绘作为角色参考；非透明背景。展示版本仅做 WebP 编码压缩，未裁剪或重新绘制。以下为最终生成提示词：

```text
Use case: stylized-concept.
Asset type: final wide GitHub personal-profile masthead, landscape 2:1 aspect ratio, approximately 2048 by 1024. This is a NEW composed illustration and editorial graphic, not a website screenshot or mockup.
Reference image role: character-identity reference for Springfield (春田) from Girls' Frontline. Faithfully preserve her recognizable adult appearance: long warm chestnut/auburn hair, gentle green eyes, soft mature smile, her distinctive side hair loops, navy blue military uniform with gold buttons, white blouse and white skirt, small burgundy neck ribbon, white gloves and diagonal white sash. Keep her character recognizable. Do not copy the reference pose. No need for a weapon.
Primary request: An exceptionally art-directed, stylish anime developer personal-page hero titled zlcwwhq. Concept: OFF-DUTY TERMINAL, a quiet late-night refuge between tactical operations and writing code. Balance Arknights-inspired utilitarian editorial typography with the warmth of Springfield from Girls' Frontline.
Scene: rain streaked windows in a dim retro-futuristic café inside a mobile landship. Distant blue-gray industrial towers, quiet suspended dust and rain reflections. A dark wood counter and a single steaming white coffee cup in the lower right.
Composition: Springfield occupies the right 45 percent, waist-up or mid-thigh portrait, face near upper-right thirds, looking gently toward the viewer. One gloved hand resting naturally near the cup, anatomically coherent. No character overlap with the left text region. Background has natural depth, beautifully painted 2D anime key visual, crisp ink lines, subtle textured shading, not 3D or photoreal.
Graphic design: left 50 percent is very dark ink navy with a sophisticated softly blended transition into the illustration, spacious editorial layout. Hairline blueprint grids, fine asymmetric rules, tiny crosshair registration marks, one narrow burnt-orange tab, a few precise amber blocks. Use restrained gray-beige print texture, not noisy cyberpunk. Large quiet typography, no rounded UI cards or fake website components.
Text exactly, beautifully typeset, no other text:
Top left small monospaced: "PERSONAL ARCHIVE / 001"
Middle left enormous warm ivory lowercase wordmark: "zlcwwhq"
Under wordmark medium uppercase widely spaced: "OFF-DUTY TERMINAL"
Lower left smaller clean text across two lines:
"ENGINEERING BY DAY."
"WORLDS BEYOND THE SCREEN."
Bottom left microtext: "ARKNIGHTS / GIRLS' FRONTLINE"
Bottom right small caption, unobtrusive: "SPRINGFIELD / 春田"
Color palette: deep ink #111b25, slate blue, ivory #eee8db, restrained ochre amber #c99557; warm amber light catches auburn hair and her shoulder, blue light from rain window. Face and green eyes remain luminous, inviting and crisp.
Constraints: elegant anime art magazine cover quality; strong distinctive identity; all typography legible and exactly spelled; no logos copied from either game; no signatures, no watermarks; no nudity, no sexualization, no clutter. This is a personal fan illustration.
```
