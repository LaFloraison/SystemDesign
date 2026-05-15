# 党团班一体化系统 设计系统 / Design System

> 版本 1.0 | 2026-05-15
> 技术栈: Django Templates + HTMX + Alpine.js (服务端渲染 SSR)

---

## 1. 色彩系统 / Color Palette

### 1.1 主题色 / Primary — "赤诚红"

党团组织的核心识别色，传递庄重、信仰与凝聚力。**避免**大面积用作背景，主要用于关键操作按钮、选中态、核心图标。

| Tone | Hex Code | CSS Variable                   | Usage                        |
|------|----------|-------------------------------|------------------------------|
| 50   | #FFF0F0  | `--color-primary-50`          | Red-tinted surface           |
| 100  | #FFDBDB  | `--color-primary-100`         | Tag bg, subtle highlight     |
| 200  | #FFB8B8  | `--color-primary-200`         | Progress bar bg              |
| 300  | #FF8585  | `--color-primary-300`         | Border (active)              |
| 400  | #FF5252  | `--color-primary-400`         | Focus ring                   |
| 500  | #E53935  | `--color-primary-500` (BASE)  | Primary button, link, icon   |
| 600  | #CC2F2B  | `--color-primary-600`         | Button hover                 |
| 700  | #B02520  | `--color-primary-700`         | Button active / pressed      |
| 800  | #8B1B18  | `--color-primary-800`         | Dark mode primary            |
| 900  | #6B1210  | `--color-primary-900`         | Deep emphasis text           |

### 1.2 辅助色 / Accent — "金穗黄"

团徽、党徽中金色的提取，用于评分星级、推优标识、荣誉标签。

| Tone | Hex Code | CSS Variable                   | Usage                     |
|------|----------|-------------------------------|---------------------------|
| 50   | #FFFBE6  | `--color-accent-50`           | Highlight surface         |
| 100  | #FFF3B0  | `--color-accent-100`          | Light gold badge bg       |
| 200  | #FFE066  | `--color-accent-200`          | Star rating (empty)       |
| 300  | #FFCA28  | `--color-accent-300`          | Star rating (full)        |
| 400  | #FFB300  | `--color-accent-400`          | Accent border             |
| 500  | #FF8F00  | `--color-accent-500` (BASE)   | Award badge, trophy icon  |
| 600  | #E67E00  | `--color-accent-600`          | Hover state               |
| 700  | #CC6E00  | `--color-accent-700`          | Active state              |

### 1.3 功能色 / Functional Colors

| Color    | Hex (Base) | Light Background | Dark Text   | Usage                              |
|----------|------------|-----------------|-------------|------------------------------------|
| Success  | `#16A34A`  | `#F0FDF4`       | `#166534`   | 通过、完成、正常出勤                |
| Warning  | `#EA580C`  | `#FFF7ED`       | `#9A3412`   | 待审核、注意、迟到                  |
| Danger   | `#DC2626`  | `#FEF2F2`       | `#991B1B`   | 删除、拒绝、缺勤、违纪              |
| Info     | `#2563EB`  | `#EFF6FF`       | `#1E40AF`   | 消息提示、帮助信息                  |

### 1.4 背景色 / Background Colors

| Token                 | Hex Code | Usage                                       |
|-----------------------|----------|---------------------------------------------|
| `--bg-page`           | `#F3F4F6` | 全局页面背景 (浅灰，降低视觉疲劳)            |
| `--bg-card`           | `#FFFFFF` | 卡片、表格、模态框背景                       |
| `--bg-sidebar`        | `#1E293B` | 侧边导航栏 (深蓝灰，稳定感)                  |
| `--bg-sidebar-hover`  | `#334155` | 侧边栏悬停                                   |
| `--bg-sidebar-active` | `#E53935` | 侧边栏激活项 (主色)                          |
| `--bg-input`          | `#FFFFFF` | 输入框背景                                   |
| `--bg-input-disabled` | `#F9FAFB` | 禁用输入框背景                               |
| `--bg-tooltip`        | `#1F2937` | 工具提示背景                                 |

### 1.5 文字色 / Text Colors

| Token                  | Hex Code | Usage                           |
|------------------------|----------|----------------------------------|
| `--text-primary`       | `#111827` | 正文、标题、重要信息              |
| `--text-secondary`     | `#6B7280` | 辅助说明、描述文字                |
| `--text-muted`         | `#9CA3AF` | 占位符、禁用文字、水印            |
| `--text-inverse`       | `#FFFFFF` | 深色背景上的文字 (侧边栏、按钮)   |
| `--text-link`          | `#E53935` | 超链接 (同主色)                   |

### 1.6 边框色 / Border Colors

| Token                  | Hex Code | Usage                                |
|------------------------|----------|--------------------------------------|
| `--border-default`    | `#E5E7EB` | 默认边框 (input, table, card)         |
| `--border-light`      | `#F3F4F6` | 浅分隔线                              |
| `--border-focus`      | `#E53935` | 聚焦边框 (同主色)                     |
| `--border-error`      | `#DC2626` | 错误状态边框                          |

---

## 2. 字体排版 / Typography

### 2.1 字体族

```
font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", "Hiragino Sans GB", system-ui, -apple-system, sans-serif;
monospace: "JetBrains Mono", "SF Mono", "Cascadia Code", "Consolas", monospace;
```

**CDN 引入 (Google Fonts):**

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

> 备用方案：国内网络环境下可使用 `https://fonts.loli.net` 镜像或直接依赖系统字体 `PingFang SC` / `Microsoft YaHei`。

### 2.2 字号阶梯 / Font Size Scale

| Token       | rem   | px (16px base) | Usage                               |
|-------------|-------|----------------|--------------------------------------|
| `--text-xs` | 0.75  | 12px           | Badge tiny, table footnote, tooltip  |
| `--text-sm` | 0.875 | 14px           | Table cell, form label, badge        |
| `--text-base`| 1.0  | 16px           | Body, input text, button, paragraph  |
| `--text-lg` | 1.125 | 18px           | Card title, modal title, nav item    |
| `--text-xl` | 1.25  | 20px           | Page h3, stat card label             |
| `--text-2xl`| 1.5   | 24px           | Page h2, modal title (large)         |
| `--text-3xl`| 1.875 | 30px           | Page h1, stat card value             |
| `--text-4xl`| 2.25  | 36px           | Dashboard hero number                |

### 2.3 字重 / Font Weights

| Weight | Value | Usage                                |
|--------|-------|--------------------------------------|
| Light  | 300   | Large hero numbers only              |
| Normal | 400   | Body text, descriptions, labels      |
| Medium | 500   | Subtle emphasis, nav items, captions |
| Semibold| 600  | Headings, button text, card titles   |
| Bold   | 700   | Strong emphasis (use sparingly)      |

### 2.4 行高 / Line Heights

| Token         | Value | Usage                             |
|---------------|-------|-----------------------------------|
| `--leading-none`    | 1     | Large display numbers, badges     |
| `--leading-tight`   | 1.25  | Headings h1-h4                    |
| `--leading-normal`  | 1.5   | Body text, form labels (default)  |
| `--leading-relaxed` | 1.625 | Long-form content, descriptions   |

### 2.5 标题样式 / Heading Styles

```css
h1 { font-size: var(--text-3xl); font-weight: 600; line-height: var(--leading-tight); color: var(--text-primary); margin-bottom: 1.5rem; }
h2 { font-size: var(--text-2xl); font-weight: 600; line-height: var(--leading-tight); color: var(--text-primary); margin-bottom: 1rem; }
h3 { font-size: var(--text-xl); font-weight: 600; line-height: var(--leading-tight); color: var(--text-primary); margin-bottom: 0.75rem; }
h4 { font-size: var(--text-lg); font-weight: 600; line-height: var(--leading-tight); color: var(--text-primary); margin-bottom: 0.5rem; }
h5 { font-size: var(--text-base); font-weight: 600; line-height: var(--leading-normal); color: var(--text-primary); margin-bottom: 0.5rem; }
h6 { font-size: var(--text-sm); font-weight: 600; line-height: var(--leading-normal); color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; }
```

---

## 3. 间距系统 / Spacing System

**基础单位: 4px (0.25rem)**

所有间距为该基础单位的整数倍，确保视觉节奏一致。

### 3.1 间距标尺

| Token   | rem  | px   | Usage                                          |
|---------|------|------|------------------------------------------------|
| `--s-0` | 0    | 0    | No spacing                                     |
| `--s-1` | 0.25 | 4px  | Icon-to-text gap, inline tag gap               |
| `--s-2` | 0.5  | 8px  | Tight inner padding, inline form gap           |
| `--s-3` | 0.75 | 12px | Element gap in a row                           |
| `--s-4` | 1.0  | 16px | Card padding, form group gap, table cell pad   |
| `--s-5` | 1.25 | 20px | Section content gap                            |
| `--s-6` | 1.5  | 24px | Section vertical gap, modal padding            |
| `--s-8` | 2.0  | 32px | Page content padding, large section gap        |
| `--s-10`| 2.5  | 40px | Hero section spacing                           |
| `--s-12`| 3.0  | 48px | Page-level margin, footer gap                  |
| `--s-16`| 4.0  | 64px | Ultra-large separation                         |

### 3.2 常用场景间距速查

| 场景                   | 值         |
|------------------------|------------|
| 卡片内边距 (padding)    | `16px 20px` (`--s-4` `--s-5` 纵向优先) |
| 卡片之间间距 (gap)      | `20px` (`--s-5`) |
| 表单组件纵向间距        | `20px` (`--s-5`) |
| 表单标签与输入框间距     | `8px` (`--s-2`) |
| 表格单元格内边距        | `12px 16px` |
| Section 纵向间距         | `32px` (`--s-8`) |
| 页面内容区 padding      | `24px` (`--s-6`) |
| 按钮内边距 (md)         | `8px 20px` |

---

## 4. 组件样式 / Component Styles

### 4.1 按钮 / Buttons

按钮使用 **渐变背景 + box-shadow** 增强层次感，悬浮时有轻微上浮效果。

#### 基础样式 (所有按钮共享)

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: inherit;
  font-weight: 500;
  border: 1.5px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  white-space: nowrap;
  user-select: none;
  outline: none;
}
.btn:focus-visible {
  box-shadow: 0 0 0 3px rgba(229, 57, 53, 0.35);
}
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}
```

#### 尺寸变体

| Size | Class       | Height | Padding       | Font Size       |
|------|-------------|--------|---------------|------------------|
| sm   | `.btn-sm`   | 32px   | `6px 14px`    | `var(--text-sm)` |
| md   | `.btn-md`   | 38px   | `8px 20px`    | `var(--text-sm)` |
| lg   | `.btn-lg`   | 46px   | `12px 28px`   | `var(--text-base)` |

#### 主按钮 / Primary (渐变红)

```css
.btn-primary {
  color: #FFFFFF;
  background: linear-gradient(135deg, #E53935 0%, #C62828 100%);
  border-color: transparent;
  box-shadow: 0 2px 8px rgba(229, 57, 53, 0.35);
}
.btn-primary:hover {
  background: linear-gradient(135deg, #EF5350 0%, #D32F2F 100%);
  box-shadow: 0 4px 14px rgba(229, 57, 53, 0.45);
  transform: translateY(-1px);
}
.btn-primary:active {
  background: linear-gradient(135deg, #C62828 0%, #B71C1C 100%);
  box-shadow: 0 1px 4px rgba(229, 57, 53, 0.3);
  transform: translateY(0);
}
```

#### 次要按钮 / Secondary

```css
.btn-secondary {
  color: #FFFFFF;
  background: linear-gradient(135deg, #475569 0%, #334155 100%);
  border-color: transparent;
  box-shadow: 0 2px 8px rgba(51, 65, 85, 0.3);
}
.btn-secondary:hover {
  background: linear-gradient(135deg, #64748B 0%, #475569 100%);
  box-shadow: 0 4px 14px rgba(51, 65, 85, 0.4);
  transform: translateY(-1px);
}
.btn-secondary:active {
  background: linear-gradient(135deg, #334155 0%, #1E293B 100%);
  transform: translateY(0);
}
```

#### 线框按钮 / Outline

```css
.btn-outline {
  color: var(--color-primary-500);
  background: #FFFFFF;
  border-color: var(--color-primary-500);
}
.btn-outline:hover {
  background: var(--color-primary-50);
  border-color: var(--color-primary-600);
  color: var(--color-primary-600);
}
.btn-outline:active {
  background: var(--color-primary-100);
  border-color: var(--color-primary-700);
  color: var(--color-primary-700);
}
```

#### 危险按钮 / Danger

```css
.btn-danger {
  color: #FFFFFF;
  background: linear-gradient(135deg, #DC2626 0%, #B91C1C 100%);
  border-color: transparent;
  box-shadow: 0 2px 8px rgba(220, 38, 38, 0.3);
}
.btn-danger:hover {
  background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
  box-shadow: 0 4px 14px rgba(220, 38, 38, 0.4);
  transform: translateY(-1px);
}
```

#### 文字按钮 / Ghost

```css
.btn-ghost {
  color: var(--text-secondary);
  background: transparent;
  border-color: transparent;
}
.btn-ghost:hover {
  background: #F3F4F6;
  color: var(--text-primary);
}
.btn-ghost:active {
  background: #E5E7EB;
}
```

### 4.2 卡片 / Cards

```css
.card {
  background: #FFFFFF;
  border: 1px solid var(--border-default);
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
  transition: box-shadow 0.25s ease, transform 0.25s ease;
}
.card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08), 0 2px 6px rgba(0, 0, 0, 0.04);
  transform: translateY(-2px);
}
```

**卡片变体:**
- `.card-flat` — 无边框无阴影，仅作为内容分组
- `.card-interactive` — 默认样式 + hover 效果 (用于可点击卡片)
- `.card-compact` — padding 改为 `12px 16px`

### 4.3 统计卡片 / Stat Cards

```html
<div class="stat-card">
  <div class="stat-card__icon-container">
    <i class="bi bi-people-fill stat-card__icon"></i>
  </div>
  <div class="stat-card__body">
    <span class="stat-card__label">党员总数</span>
    <span class="stat-card__value">128</span>
    <span class="stat-card__trend stat-card__trend--up">
      <i class="bi bi-arrow-up-short"></i> 12.5%
    </span>
  </div>
</div>
```

```css
.stat-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: #FFFFFF;
  border: 1px solid var(--border-default);
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
  transition: box-shadow 0.25s ease, transform 0.25s ease;
}
.stat-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}
.stat-card__icon-container {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: linear-gradient(135deg, #FFF0F0 0%, #FFDBDB 100%);
  color: var(--color-primary-500);
}
.stat-card__icon {
  font-size: 22px;
}
.stat-card__label {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  font-weight: 400;
  display: block;
  margin-bottom: 4px;
}
.stat-card__value {
  font-size: var(--text-3xl);
  font-weight: 700;
  color: var(--text-primary);
  line-height: var(--leading-none);
  display: block;
}
.stat-card__trend {
  font-size: var(--text-xs);
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 2px;
  margin-top: 6px;
}
.stat-card__trend--up   { color: #16A34A; }
.stat-card__trend--down { color: #DC2626; }
.stat-card__trend--flat { color: var(--text-muted); }
```

**统计卡片颜色变体 (修改 icon-container 背景和图标色):**
- `.stat-card--accent` — 金色主题 (推优、星级)
- `.stat-card--info` — 蓝色主题 (通知、消息)
- `.stat-card--success` — 绿色主题 (出勤率)
- `.stat-card--warning` — 橙色主题 (待办事项)

### 4.4 表单 / Forms

```css
.form-group {
  margin-bottom: 20px;
}
.form-label {
  display: block;
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: 8px;
}
.form-label--required::after {
  content: " *";
  color: #DC2626;
}
.form-input {
  width: 100%;
  height: 40px;
  padding: 0 12px;
  font-size: var(--text-sm);
  font-family: inherit;
  color: var(--text-primary);
  background: #FFFFFF;
  border: 1.5px solid var(--border-default);
  border-radius: 8px;
  outline: none;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.form-input::placeholder {
  color: var(--text-muted);
}
.form-input:hover {
  border-color: #D1D5DB;
}
.form-input:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(229, 57, 53, 0.15);
}
.form-input--error {
  border-color: #DC2626;
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}
.form-input:disabled {
  background: #F9FAFB;
  color: var(--text-muted);
  cursor: not-allowed;
}
.form-error-text {
  font-size: var(--text-xs);
  color: #DC2626;
  margin-top: 6px;
  display: flex;
  align-items: center;
  gap: 4px;
}
.form-hint {
  font-size: var(--text-xs);
  color: var(--text-muted);
  margin-top: 6px;
}

/* Select 与 Input 保持一致 */
.form-select {
  width: 100%;
  height: 40px;
  padding: 0 36px 0 12px;
  font-size: var(--text-sm);
  font-family: inherit;
  color: var(--text-primary);
  background: #FFFFFF url("data:image/svg+xml,...") no-repeat right 12px center;
  border: 1.5px solid var(--border-default);
  border-radius: 8px;
  appearance: none;
  cursor: pointer;
}

/* Textarea */
.form-textarea {
  width: 100%;
  min-height: 100px;
  padding: 10px 12px;
  font-size: var(--text-sm);
  font-family: inherit;
  line-height: var(--leading-normal);
  resize: vertical;
  border: 1.5px solid var(--border-default);
  border-radius: 8px;
  outline: none;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.form-textarea:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(229, 57, 53, 0.15);
}

/* Checkbox / Radio */
.form-check {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: var(--text-sm);
  color: var(--text-primary);
  cursor: pointer;
}
.form-check input[type="checkbox"],
.form-check input[type="radio"] {
  width: 16px;
  height: 16px;
  accent-color: var(--color-primary-500);
  cursor: pointer;
}
```

### 4.5 表格 / Tables

```css
.table-container {
  overflow-x: auto;
  border: 1px solid var(--border-default);
  border-radius: 12px;
  background: #FFFFFF;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}

.table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--text-sm);
}

.table thead {
  background: #F9FAFB;
  border-bottom: 2px solid var(--border-default);
}

.table thead th {
  padding: 12px 16px;
  text-align: left;
  font-weight: 600;
  font-size: var(--text-xs);
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  white-space: nowrap;
  user-select: none;
}

.table thead th.sortable {
  cursor: pointer;
}
.table thead th.sortable:hover {
  color: var(--text-primary);
}
.table thead th.sortable .sort-icon {
  display: inline-block;
  margin-left: 4px;
  font-size: 10px;
  opacity: 0.4;
}
.table thead th.sorted .sort-icon {
  opacity: 1;
  color: var(--color-primary-500);
}

.table tbody tr {
  border-bottom: 1px solid var(--border-light);
  transition: background-color 0.15s ease;
}

.table tbody tr:last-child {
  border-bottom: none;
}

.table tbody tr:hover {
  background: #FAFAFA;
}

.table tbody td {
  padding: 12px 16px;
  color: var(--text-primary);
  vertical-align: middle;
  white-space: nowrap;
}

.table tbody td.text-muted {
  color: var(--text-secondary);
}

/* 表格内操作按钮 */
.table .row-actions {
  display: flex;
  gap: 8px;
}

/* 空状态 */
.table-empty {
  text-align: center;
  padding: 48px 16px !important;
  color: var(--text-muted);
}

/* 表格内头像+文字 */
.table-avatar-cell {
  display: flex;
  align-items: center;
  gap: 10px;
}
.table-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
  background: #F3F4F6;
  flex-shrink: 0;
}
```

### 4.6 徽章 / Badges

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 10px;
  font-size: var(--text-xs);
  font-weight: 500;
  line-height: 1.4;
  border-radius: 9999px;  /* 胶囊形 */
  white-space: nowrap;
}

.badge--pending  { background: #FFF7ED; color: #9A3412; }
.badge--approved { background: #F0FDF4; color: #166534; }
.badge--rejected { background: #FEF2F2; color: #991B1B; }
.badge--active   { background: #F0FDF4; color: #166534; }
.badge--inactive { background: #F3F4F6; color: #6B7280; }
.badge--info     { background: #EFF6FF; color: #1E40AF; }
.badge--warning  { background: #FFF7ED; color: #9A3412; }

/* 带小圆点的 Badge */
.badge--dot::before {
  content: "";
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}
```

### 4.7 导航 / Navigation

侧边栏采用深色背景 (`#1E293B`)，与白色内容区形成清晰边界。

```css
/* === 侧边栏布局 === */
.sidebar {
  width: 250px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 40;
  background: var(--bg-sidebar);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
  transition: width 0.3s ease;
}

.sidebar--collapsed {
  width: 72px;
}

/* Logo 区域 */
.sidebar__brand {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 20px 20px;
  height: 64px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  flex-shrink: 0;
  overflow: hidden;
  white-space: nowrap;
}
.sidebar__brand-logo {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  flex-shrink: 0;
}
.sidebar__brand-text {
  font-size: var(--text-base);
  font-weight: 600;
  color: #FFFFFF;
  transition: opacity 0.2s ease;
}
.sidebar--collapsed .sidebar__brand-text {
  opacity: 0;
  width: 0;
}

/* 导航分组 */
.sidebar__section-label {
  padding: 16px 20px 6px;
  font-size: var(--text-xs);
  font-weight: 600;
  color: #64748B;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  overflow: hidden;
  white-space: nowrap;
}
.sidebar--collapsed .sidebar__section-label {
  opacity: 0;
}

/* 导航项 */
.sidebar__nav {
  flex: 1;
  padding: 8px 12px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.sidebar__item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 8px;
  color: #94A3B8;
  text-decoration: none;
  font-size: var(--text-sm);
  font-weight: 400;
  transition: all 0.2s ease;
  white-space: nowrap;
  overflow: hidden;
}
.sidebar__item i {
  font-size: 18px;
  width: 20px;
  text-align: center;
  flex-shrink: 0;
}
.sidebar__item span {
  transition: opacity 0.2s ease;
}
.sidebar--collapsed .sidebar__item span {
  opacity: 0;
  width: 0;
}
.sidebar__item:hover {
  background: var(--bg-sidebar-hover);
  color: #E2E8F0;
}
/* 激活态 (主色背景) */
.sidebar__item--active {
  background: var(--bg-sidebar-active) !important;
  color: #FFFFFF !important;
  font-weight: 500;
  box-shadow: 0 2px 8px rgba(229, 57, 53, 0.4);
}
/* 子菜单项 (缩进) */
.sidebar__subitem {
  padding-left: 44px;
  font-size: var(--text-xs);
}

/* 用户信息区 */
.sidebar__user {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  flex-shrink: 0;
}
.sidebar__user-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  flex-shrink: 0;
}
.sidebar__user-info {
  overflow: hidden;
}
.sidebar__user-name {
  font-size: var(--text-sm);
  font-weight: 500;
  color: #FFFFFF;
  white-space: nowrap;
}
.sidebar__user-role {
  font-size: var(--text-xs);
  color: #94A3B8;
  white-space: nowrap;
}
```

**顶栏 (Topbar):**

```css
.topbar {
  height: 64px;
  padding: 0 24px;
  background: #FFFFFF;
  border-bottom: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 30;
}
.topbar__left {
  display: flex;
  align-items: center;
  gap: 16px;
}
.topbar__toggle {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  background: transparent;
  color: var(--text-secondary);
  border-radius: 8px;
  cursor: pointer;
  font-size: 20px;
}
.topbar__toggle:hover {
  background: #F3F4F6;
  color: var(--text-primary);
}
.topbar__title {
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--text-primary);
}
.topbar__right {
  display: flex;
  align-items: center;
  gap: 12px;
}
/* 通知铃铛 */
.topbar__notification-btn {
  position: relative;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  background: transparent;
  color: var(--text-secondary);
  border-radius: 8px;
  cursor: pointer;
  font-size: 18px;
  transition: all 0.2s;
}
.topbar__notification-btn:hover {
  background: #F3F4F6;
  color: var(--text-primary);
}
.topbar__notification-dot {
  position: absolute;
  top: 6px;
  right: 6px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #DC2626;
  border: 2px solid #FFFFFF;
}
```

### 4.8 模态框 / Modals

```css
/* 遮罩层 */
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 50;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(2px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  animation: fadeIn 0.2s ease;
}

/* 模态框本体 */
.modal {
  background: #FFFFFF;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 520px;
  max-height: 85vh;
  overflow-y: auto;
  animation: scaleIn 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.modal--sm { max-width: 400px; }
.modal--lg { max-width: 720px; }
.modal--xl { max-width: 960px; }

.modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px;
  border-bottom: 1px solid var(--border-light);
}
.modal__title {
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--text-primary);
}
.modal__close {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  background: transparent;
  color: var(--text-muted);
  border-radius: 6px;
  cursor: pointer;
  font-size: 18px;
  transition: all 0.15s;
}
.modal__close:hover {
  background: #F3F4F6;
  color: var(--text-primary);
}

.modal__body {
  padding: 20px 24px;
  font-size: var(--text-sm);
  color: var(--text-primary);
  line-height: var(--leading-relaxed);
}

.modal__footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  padding: 16px 24px;
  border-top: 1px solid var(--border-light);
  background: #F9FAFB;
  border-radius: 0 0 16px 16px;
}
```

### 4.9 Toast 通知 / Toast Notifications

位置：屏幕右上角，距顶部 20px，距右侧 20px。

```css
.toast-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 100;
  display: flex;
  flex-direction: column;
  gap: 10px;
  pointer-events: none;
}

.toast {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 18px;
  background: #FFFFFF;
  border: 1px solid var(--border-default);
  border-radius: 10px;
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.12);
  font-size: var(--text-sm);
  color: var(--text-primary);
  pointer-events: auto;
  min-width: 300px;
  max-width: 420px;
  animation: toastSlideIn 0.35s cubic-bezier(0.21, 1.02, 0.73, 1) forwards;
  position: relative;
  overflow: hidden;
}
.toast--success { border-left: 4px solid #16A34A; }
.toast--error   { border-left: 4px solid #DC2626; }
.toast--warning { border-left: 4px solid #EA580C; }
.toast--info    { border-left: 4px solid #2563EB; }

.toast__icon {
  font-size: 18px;
  flex-shrink: 0;
}
.toast--success .toast__icon { color: #16A34A; }
.toast--error   .toast__icon { color: #DC2626; }
.toast--warning .toast__icon { color: #EA580C; }
.toast--info    .toast__icon { color: #2563EB; }

.toast__content {
  flex: 1;
  line-height: 1.4;
}
.toast__close {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  border: none;
  background: transparent;
  color: var(--text-muted);
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

/* Toast 进度条 (自动消失) */
.toast__progress {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  background: var(--color-primary-500);
  animation: toastProgress 4s linear forwards;
}
.toast--success .toast__progress { background: #16A34A; }
.toast--error   .toast__progress { background: #DC2626; }
.toast--warning .toast__progress { background: #EA580C; }
.toast--info    .toast__progress { background: #2563EB; }
```

---

## 5. 布局 / Layout

### 5.1 整体结构

```
+--------------------------------------------------+
|  Sidebar  |  Topbar                              |
|  (fixed)  |  +----------------------------------+
|           |  |  Content Area                     |
|  250px    |  |  (scrollable)                     |
|           |  |                                   |
|           |  |                                   |
+-----------+--+-----------------------------------+
```

### 5.2 关键尺寸

| 元素                | 值       | CSS Variable            |
|---------------------|----------|--------------------------|
| 侧边栏展开宽度       | 250px    | `--sidebar-width`        |
| 侧边栏折叠宽度       | 72px     | `--sidebar-collapsed`   |
| 顶栏高度            | 64px     | `--topbar-height`        |
| 内容区最大宽度       | 1280px   | `--content-max-width`    |
| 内容区内边距        | 24px     | —                        |

```css
:root {
  --sidebar-width: 250px;
  --sidebar-collapsed: 72px;
  --topbar-height: 64px;
  --content-max-width: 1280px;
}

.main-layout {
  display: flex;
  min-height: 100vh;
}

.main-content {
  margin-left: var(--sidebar-width);
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  transition: margin-left 0.3s ease;
}

.sidebar--collapsed ~ .main-content {
  margin-left: var(--sidebar-collapsed);
}

.content-area {
  flex: 1;
  padding: 24px;
  max-width: var(--content-max-width);
  width: 100%;
}
```

### 5.3 响应式断点 / Responsive Breakpoints

| 断点名  | 宽度      | 行为                                           |
|---------|-----------|------------------------------------------------|
| `xs`    | < 640px   | 手机竖屏                                       |
| `sm`    | >= 640px  | 手机横屏/小平板                                |
| `md`    | >= 768px  | 平板竖屏: 侧边栏默认折叠                       |
| `lg`    | >= 1024px | 桌面: 侧边栏展开                               |
| `xl`    | >= 1280px | 大桌面                                         |
| `2xl`   | >= 1536px | 超大屏: 内容居中，两侧留白                     |

```css
/* 平板及以下 (md): 侧边栏变为滑出式 overlay */
@media (max-width: 1023px) {
  .sidebar {
    transform: translateX(-100%);
    box-shadow: none;
    transition: transform 0.3s ease;
  }
  .sidebar--mobile-open {
    transform: translateX(0);
    box-shadow: 4px 0 20px rgba(0, 0, 0, 0.3);
  }
  .main-content {
    margin-left: 0 !important;
  }

  /* 移动端侧边栏打开时的遮罩 */
  .sidebar-overlay {
    position: fixed;
    inset: 0;
    z-index: 39;
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(1px);
    animation: fadeIn 0.2s ease;
  }

  .content-area {
    padding: 16px;
  }
}
```

### 5.4 常用布局栅格 (CSS Grid 辅助)

```css
/* 仪表盘统计卡片网格 */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 20px;
}

/* 两栏布局 (侧边详情) */
.two-column {
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 24px;
  align-items: start;
}
@media (max-width: 1023px) {
  .two-column {
    grid-template-columns: 1fr;
  }
}

/* 三等分 */
.three-column {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
@media (max-width: 767px) {
  .three-column {
    grid-template-columns: 1fr;
  }
}
```

---

## 6. 图标系统 / Iconography

### 6.1 图标库

使用 **Bootstrap Icons** (v1.11+)，通过 CDN 引入。

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
```

### 6.2 图标尺寸

| 上下文           | 类名              | Font Size | 示例                     |
|------------------|-------------------|-----------|--------------------------|
| 内联文本图标     | —                 | 1em       | `<i class="bi bi-check-circle-fill"></i>` 用于 Badge 内 |
| 按钮内图标       | —                 | 1em       | 跟随按钮文字大小           |
| 侧边栏导航       | —                 | 18px      | `<i class="bi bi-house-door-fill"></i>` |
| 统计卡片         | —                 | 22px      | 见 stat-card 组件          |
| 顶栏功能图标     | —                 | 18px      | 铃铛、搜索等              |
| 空状态插图图标   | `.icon-2xl`       | 48px      | 表格空状态                |
| 页面装饰图标     | `.icon-3xl`       | 64px      | 404页面等                 |

### 6.3 图标间距

图标与文字之间统一使用 `gap: 8px` (flex布局) 或 `margin-right: 8px`。

### 6.4 推荐图标映射

| 功能              | Bootstrap Icon                                  |
|-------------------|--------------------------------------------------|
| 首页/仪表盘        | `bi-house-door-fill` / `bi-grid-fill`            |
| 通知              | `bi-bell-fill`                                   |
| 活动管理           | `bi-calendar-event-fill`                         |
| 考勤管理           | `bi-person-check-fill`                           |
| 党团员管理         | `bi-people-fill`                                 |
| 推优评议           | `bi-star-fill`                                   |
| 公示材料           | `bi-file-earmark-text-fill`                      |
| 个人信息           | `bi-person-circle`                               |
| 设置              | `bi-gear-fill`                                   |
| 搜索              | `bi-search`                                      |
| 添加/新建         | `bi-plus-lg`                                     |
| 编辑              | `bi-pencil-square`                               |
| 删除              | `bi-trash3`                                      |
| 导出              | `bi-download`                                    |
| 刷新              | `bi-arrow-clockwise`                             |
| 更多操作           | `bi-three-dots-vertical`                         |
| 返回              | `bi-arrow-left`                                  |
| 通过/成功         | `bi-check-circle-fill`                           |
| 拒绝/失败         | `bi-x-circle-fill`                               |
| 警告              | `bi-exclamation-triangle-fill`                   |
| 信息              | `bi-info-circle-fill`                            |
| 展开              | `bi-chevron-down`                                |
| 用户/头像占位      | `bi-person-fill`                                 |
| 上传              | `bi-cloud-arrow-up`                              |
| 时间/日期         | `bi-clock`                                       |
| 位置              | `bi-geo-alt-fill`                                |
| 附件              | `bi-paperclip`                                   |
| 成绩/评分         | `bi-bar-chart-fill`                              |

---

## 7. 动效 / Animations

### 7.1 核心原则

- **快速响应**: 交互动画的持续时间不超过 300ms
- **有意义**: 动效服务于引导注意力，不滥用
- **尊重偏好**: 检测 `prefers-reduced-motion` 并关闭动画

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 7.2 CSS 变量定义

```css
:root {
  --transition-fast:    150ms;
  --transition-base:    200ms;
  --transition-slow:    300ms;
  --transition-ease:    cubic-bezier(0.4, 0, 0.2, 1);
  --transition-ease-in: cubic-bezier(0.4, 0, 1, 1);
  --transition-ease-out:cubic-bezier(0, 0, 0.2, 1);
  --transition-spring:  cubic-bezier(0.175, 0.885, 0.32, 1.275);
  --transition-bounce:  cubic-bezier(0.21, 1.02, 0.73, 1);
}
```

### 7.3 关键帧动画

```css
/* 淡入 */
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* 缩放入场 (模态框) */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.92) translateY(10px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

/* Toast 滑入 */
@keyframes toastSlideIn {
  from {
    opacity: 0;
    transform: translateX(100%) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
}

/* Toast 滑出 */
@keyframes toastSlideOut {
  from {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
  to {
    opacity: 0;
    transform: translateX(100%) scale(0.95);
  }
}

/* 骨架屏 shimmer */
@keyframes shimmer {
  0%   { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* 淡入上移 (页面加载) */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 进度条 */
@keyframes toastProgress {
  from { width: 100%; }
  to   { width: 0%; }
}

/* 旋转 (加载器) */
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
```

### 7.4 页面加载效果

内容卡片使用**交错入场**动画，每个卡片延迟 50ms:

```css
.content-card {
  animation: fadeInUp 0.4s var(--transition-ease-out) both;
}
.content-card:nth-child(1) { animation-delay: 0ms; }
.content-card:nth-child(2) { animation-delay: 50ms; }
.content-card:nth-child(3) { animation-delay: 100ms; }
.content-card:nth-child(4) { animation-delay: 150ms; }
.content-card:nth-child(5) { animation-delay: 200ms; }
.content-card:nth-child(6) { animation-delay: 250ms; }
```

### 7.5 动效速查表

| 交互场景            | 属性                     | 时长  | 缓动                      |
|---------------------|--------------------------|-------|---------------------------|
| 按钮 hover          | background, transform    | 200ms | ease                      |
| 卡片 hover          | box-shadow, transform    | 250ms | ease                      |
| 输入框 focus         | border-color, box-shadow | 200ms | ease                      |
| 侧边栏切换          | width / transform        | 300ms | ease                      |
| 模态框打开           | opacity, transform       | 250ms | spring                    |
| 模态框关闭           | opacity                  | 150ms | ease-in                   |
| Toast 进入           | opacity, transform       | 350ms | bounce                    |
| Toast 退出           | opacity, transform       | 200ms | ease-in                   |
| 下拉菜单展开         | opacity, transform       | 200ms | ease-out                  |
| 页面加载卡片         | opacity, transform       | 400ms | ease-out (staggered)      |
| Tab 切换指示器       | left / width             | 250ms | ease                      |
| HTMX 内容交换        | opacity                  | 200ms | ease                      |

### 7.6 HTMX 动画集成

```css
/* HTMX 请求中 - 内容区域淡出 */
.htmx-swapping {
  opacity: 0;
  transition: opacity 200ms ease;
}

/* HTMX 新内容入场 */
.htmx-settling {
  opacity: 1;
}
```

---

## 8. 暗色模式 / Dark Mode (Optional)

当用户系统偏好为深色模式时自动切换。通过 `prefers-color-scheme: dark` 媒体查询实现，也可通过 JS Toggle 手动切换。

### 8.1 暗色模式色彩映射

```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg-page:           #0F172A;
    --bg-card:           #1E293B;
    --bg-sidebar:        #0F172A;
    --bg-sidebar-hover:  #1E293B;
    --bg-input:          #1E293B;
    --bg-input-disabled: #334155;

    --text-primary:      #F1F5F9;
    --text-secondary:    #94A3B8;
    --text-muted:        #64748B;

    --border-default:    #334155;
    --border-light:      #1E293B;

    /* 浅色背景的 Badge 在暗色下加深 */
    /* Success: #052E16 bg, #86EFAC text */
    /* Warning: #431407 bg, #FDBA74 text */
    /* Danger:  #450A0A bg, #FCA5A5 text */
    /* Info:    #172554 bg, #93C5FD text */
  }

  .card,
  .stat-card,
  .table {
    box-shadow: none;
  }

  .table thead {
    background: #1E293B;
  }

  .table tbody tr:hover {
    background: #1E293B;
  }

  .topbar {
    background: #1E293B;
    border-color: var(--border-default);
  }

  /* 图标容器保持原有的浅色渐变 (可辨识) */
}
```

### 8.2 手动切换开关

在 Topbar 提供 JS toggle，给 `<html>` 添加 `class="dark"` 以覆盖系统偏好：

```html
<button onclick="document.documentElement.classList.toggle('dark')">
  <i class="bi bi-moon-fill"></i>
</button>
```

所有暗色变量同时放在 `html.dark` 选择器下 (与 `prefers-color-scheme` 并列)。

---

## 9. 工具类 / Utility Classes

### 9.1 阴影

```css
.shadow-xs { box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
.shadow-sm { box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04); }
.shadow-md { box-shadow: 0 4px 16px rgba(0,0,0,0.08), 0 2px 6px rgba(0,0,0,0.04); }
.shadow-lg { box-shadow: 0 12px 32px rgba(0,0,0,0.12), 0 4px 10px rgba(0,0,0,0.06); }
```

### 9.2 圆角

```css
.rounded-none { border-radius: 0; }
.rounded-sm    { border-radius: 4px; }
.rounded       { border-radius: 8px; }   /* 默认 */
.rounded-md    { border-radius: 12px; }  /* 卡片 */
.rounded-lg    { border-radius: 16px; }  /* 模态框 */
.rounded-full  { border-radius: 9999px; }
```

### 9.3 常用 Flex 布局工具

```css
.flex-center { display: flex; align-items: center; justify-content: center; }
.flex-between { display: flex; align-items: center; justify-content: space-between; }
.flex-col { display: flex; flex-direction: column; }
.gap-1 { gap: 4px; }
.gap-2 { gap: 8px; }
.gap-3 { gap: 12px; }
.gap-4 { gap: 16px; }
.gap-5 { gap: 20px; }
.gap-6 { gap: 24px; }
```

### 9.4 文字工具

```css
.text-truncate { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.text-center  { text-align: center; }
.text-right   { text-align: right; }
.font-medium  { font-weight: 500; }
.font-semibold{ font-weight: 600; }
.font-bold    { font-weight: 700; }
```

---

## 10. CSS 变量完整参考

将所有设计 Token 汇总为一个 `:root` 块，方便直接复制到项目中使用。

```css
:root {
  /* === Primary (Red) === */
  --color-primary-50:  #FFF0F0;
  --color-primary-100: #FFDBDB;
  --color-primary-200: #FFB8B8;
  --color-primary-300: #FF8585;
  --color-primary-400: #FF5252;
  --color-primary-500: #E53935;
  --color-primary-600: #CC2F2B;
  --color-primary-700: #B02520;
  --color-primary-800: #8B1B18;
  --color-primary-900: #6B1210;

  /* === Accent (Gold) === */
  --color-accent-50:  #FFFBE6;
  --color-accent-100: #FFF3B0;
  --color-accent-200: #FFE066;
  --color-accent-300: #FFCA28;
  --color-accent-400: #FFB300;
  --color-accent-500: #FF8F00;
  --color-accent-600: #E67E00;
  --color-accent-700: #CC6E00;

  /* === Functional === */
  --color-success:     #16A34A;
  --color-success-bg:  #F0FDF4;
  --color-success-text:#166534;
  --color-warning:     #EA580C;
  --color-warning-bg:  #FFF7ED;
  --color-warning-text:#9A3412;
  --color-danger:      #DC2626;
  --color-danger-bg:   #FEF2F2;
  --color-danger-text: #991B1B;
  --color-info:        #2563EB;
  --color-info-bg:     #EFF6FF;
  --color-info-text:   #1E40AF;

  /* === Backgrounds === */
  --bg-page:           #F3F4F6;
  --bg-card:           #FFFFFF;
  --bg-sidebar:        #1E293B;
  --bg-sidebar-hover:  #334155;
  --bg-sidebar-active: #E53935;
  --bg-input:          #FFFFFF;
  --bg-input-disabled: #F9FAFB;
  --bg-tooltip:        #1F2937;

  /* === Text === */
  --text-primary:      #111827;
  --text-secondary:    #6B7280;
  --text-muted:        #9CA3AF;
  --text-inverse:      #FFFFFF;
  --text-link:         #E53935;

  /* === Borders === */
  --border-default:    #E5E7EB;
  --border-light:      #F3F4F6;
  --border-focus:      #E53935;
  --border-error:      #DC2626;

  /* === Typography === */
  --font-family:       "Noto Sans SC", "PingFang SC", "Microsoft YaHei", system-ui, -apple-system, sans-serif;
  --font-mono:         "JetBrains Mono", "SF Mono", "Consolas", monospace;
  --text-xs:           0.75rem;
  --text-sm:           0.875rem;
  --text-base:         1rem;
  --text-lg:           1.125rem;
  --text-xl:           1.25rem;
  --text-2xl:          1.5rem;
  --text-3xl:          1.875rem;
  --text-4xl:          2.25rem;
  --leading-none:      1;
  --leading-tight:     1.25;
  --leading-normal:    1.5;
  --leading-relaxed:   1.625;

  /* === Spacing === */
  --s-0:  0;
  --s-1:  0.25rem;
  --s-2:  0.5rem;
  --s-3:  0.75rem;
  --s-4:  1rem;
  --s-5:  1.25rem;
  --s-6:  1.5rem;
  --s-8:  2rem;
  --s-10: 2.5rem;
  --s-12: 3rem;
  --s-16: 4rem;

  /* === Layout === */
  --sidebar-width:     250px;
  --sidebar-collapsed: 72px;
  --topbar-height:     64px;
  --content-max-width: 1280px;

  /* === Transitions === */
  --transition-fast:   150ms;
  --transition-base:   200ms;
  --transition-slow:   300ms;
  --transition-ease:   cubic-bezier(0.4, 0, 0.2, 1);
  --transition-ease-in:  cubic-bezier(0.4, 0, 1, 1);
  --transition-ease-out: cubic-bezier(0, 0, 0.2, 1);
  --transition-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);
  --transition-bounce: cubic-bezier(0.21, 1.02, 0.73, 1);
}
```

---

## 11. 落地实施建议

1. **新建 `static/css/design-tokens.css`**: 复制第 10 节的 `:root` 变量块到此文件，作为所有页面的基础变量引用。
2. **新建 `static/css/components.css`**: 复制第 4 节的所有组件样式到此文件。
3. **新建 `static/css/utilities.css`**: 复制第 9 节的工具类到此文件。
4. **Django 模板 base.html**: 按顺序引入以上 CSS 文件，并在 `<head>` 中添加 Google Fonts 和 Bootstrap Icons 的 CDN 链接。
5. **HTMX 集成**: 在 base.html 的 `<head>` 中添加 `<meta name="htmx-config" content='{"globalViewTransitions":"true"}'>` 以获得原生的页面过渡动画。
6. **渐进实施**: 优先实现颜色变量、按钮、表单、卡片、表格，然后再覆盖导航和动画。
