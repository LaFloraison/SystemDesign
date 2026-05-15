# 党团班一体化系统 - Django 项目

## 项目概述
基于 Django 的党团班一体化管理系统，实现个人信息管理、通知管理、活动管理、考勤管理、党团员管理、推优评议和公示材料管理等功能。

## 技术栈
- **后端框架:** Django 6.0
- **数据库:** MySQL 8.0 (utf8mb4)
- **前端:** Django Templates + Bootstrap 5.3
- **Python版本:** 3.12
- **Conda环境:** djangoDev

## 项目路径
- **根目录:** `D:\ProjectBase\SystemDesign\Project\党团班一体化系统`
- **Django配置:** `config/settings.py`
- **应用代码:** `apps/` 目录下7个子应用
- **数据库SQL参考:** `党团班一体化系统.sql`

## 项目结构

```
党团班一体化系统/
├── manage.py                    # Django管理命令入口
├── requirements.txt             # Python依赖
├── .env                         # 环境变量(DEBUG, DB配置)
├── config/                      # Django项目配置
│   ├── settings.py              # 全局设置(数据库, 认证, 应用注册)
│   ├── urls.py                  # 根URL路由
│   └── wsgi.py
├── apps/                        # 7个功能应用
│   ├── accounts/                # 用户认证, 个人信息, 党团员档案, 成员变更审核
│   ├── notifications/           # 通知发布, 已读追踪
│   ├── activities/              # 活动发布, 报名, 签到
│   ├── attendance/              # 考勤任务, 考勤记录, 请假审核
│   ├── party/                   # 党团资料上传与审核
│   ├── recommendation/          # 推优任务, 报名, 投票
│   └── publicity/               # 公示发布, 材料提交与审核
├── templates/                   # 全局模板
│   ├── base.html                # Bootstrap导航栏+消息框架的基模板
│   └── home.html                # 角色仪表盘首页
└── static/                      # 静态文件(CSS, JS)
```

## 数据库模型 (18张表)

所有Django模型使用英文命名, 通过 `db_table` 映射到中文表名, 字段通过 `db_column` 映射到中文列名.

| 表名 | Django模型 | 所属应用 | 说明 |
|---|---|---|---|
| 用户 | User (AbstractUser) | accounts | 自定义用户, USERNAME_FIELD='student_id' |
| 党团员档案 | PartyArchive | accounts | 一对一关联用户 |
| 成员变更记录 | MemberChangeRecord | accounts | 个人信息修改审核轨迹 |
| 通知 | Notification | notifications | 通知标题/内容/截止时间 |
| 通知已读记录 | NotificationReadRecord | notifications | 追踪每条通知的已读状态 |
| 活动 | Activity | activities | 活动信息+签到码+签到截止 |
| 活动报名记录 | ActivityRegistration | activities | 活动报名/取消 |
| 活动签到记录 | ActivityCheckIn | activities | 签到码验证 |
| 考勤任务 | AttendanceTask | attendance | 考勤任务定义 |
| 考勤记录 | AttendanceRecord | attendance | 出勤/缺勤/请假记录 |
| 请假申请 | LeaveRequest | attendance | 请假申请+团支书审核 |
| 党团资料上传记录 | PartyMaterialUpload | party | 资料上传+审核流程 |
| 证明材料 | ProofMaterial | party | 证明材料管理 |
| 推优任务 | RecommendationTask | recommendation | 推优任务配置 |
| 推优报名 | RecommendationRegistration | recommendation | 报名+审核 |
| 推优投票记录 | RecommendationVote | recommendation | 投票记录(唯一约束: 任务+投票人+被投票人) |
| 公示 | Publicity | publicity | 公示发布+材料收集配置 |
| 公示材料提交记录 | PublicitySubmission | publicity | 材料提交+审核 |

## 角色权限体系

| 角色 | 字段值 | 权限概述 |
|---|---|---|
| 普通学生 | `普通学生` | 查看通知/活动/考勤, 报名活动, 签到, 请假, 上传资料, 投票 |
| 班长 | `班长` | 学生所有权限 + 审核成员变更, 发布通知/活动, 查看活动管理 |
| 团支书 | `团支书` | 班长所有权限 + 审核请假, 管理党团员档案, 发布推优/公示, 审核资料/材料 |

权限通过装饰器控制: `@role_required("班长", "团支书")` / `@role_required("团支书")`
定义在 `apps/accounts/utils.py`.

## 认证系统
- **登录方式:** 学号 + 密码
- **认证后端:** `StudentIDBackend` (`apps/accounts/backends.py`) 支持学号或用户名登录
- **User模型:** 自定义 `AbstractUser`, `USERNAME_FIELD = 'student_id'`
- **密码:** 使用 Django 内置哈希 (`make_password`)

## URL路由概览

| 前缀 | 应用 | 主要功能 |
|---|---|---|
| `/` | - | 首页仪表盘 |
| `/accounts/` | accounts | 登录/注册/个人信息/成员变更审核/党团员档案 |
| `/notifications/` | notifications | 通知列表/发布/详情/已读状态 |
| `/activities/` | activities | 活动列表/创建/报名/签到/管理 |
| `/attendance/` | attendance | 考勤记录/任务创建/录入/请假申请/审核 |
| `/party/` | party | 党团资料列表/上传/审核 |
| `/recommendation/` | recommendation | 推优任务/报名/审核/投票/结果 |
| `/publicity/` | publicity | 公示列表/发布/材料提交/审核 |

## 关键文件索引

### 核心配置
- `config/settings.py` — AUTH_USER_MODEL, MySQL配置, 应用注册
- `config/urls.py` — 根URL分发
- `.env` — 数据库连接信息

### 认证与权限
- `apps/accounts/models.py` — 自定义User模型
- `apps/accounts/backends.py` — 学号认证后端
- `apps/accounts/utils.py` — `role_required` 装饰器

### 数据种子
- `apps/accounts/management/commands/seed_data.py` — 种子命令: `python manage.py seed_data`

## 常用命令

```bash
# 激活环境
conda activate djangoDev
cd "D:\ProjectBase\SystemDesign\Project\党团班一体化系统"

# 数据库迁移
python manage.py makemigrations accounts notifications activities attendance party recommendation publicity
python manage.py migrate

# 种子数据(50个用户)
python manage.py seed_data

# 启动开发服务器
python manage.py runserver

# 创建超级用户
python manage.py createsuperuser
```

## 种子数据说明
- 2个班级: 计算机2201, 计算机2202 (各25人)
- 每班: 1班长(学号格式2024XXXX), 1团支书, 23普通学生
- 默认密码: `123456`
- 同时创建50条党团员档案记录

## UI 设计系统

### CSS 文件结构
| 文件 | 用途 |
|---|---|
| `static/css/design-tokens.css` | 80+ CSS变量: 配色、字体、间距、圆角、动画 |
| `static/css/components.css` | 组件样式: 按钮(.btn-gradient等)、卡片(.card-modern)、表单(.form-modern)、表格(.table-modern)、徽章(.badge-status) |
| `static/css/layout.css` | 布局: 侧边栏(.sidebar)、顶栏(.topbar)、内容区(.main-content)、认证页(.auth-layout)、动画(@keyframes)、响应式断点 |

### 配色体系
| 用途 | 色系 | 主色值 |
|---|---|---|
| 主操作(按钮/链接/激活) | 赤诚红 | `#E53935` |
| 侧边栏/横幅/面板 | 青蓝(Teal) | `#6CA5B3` (深变体 `#265A66`) |
| 侧边栏激活/高亮 | 浅青 | `#8FCAD7` |
| 荣誉/星级 | 金穗黄 | `#FF8F00` |
| 辅助元素 | Sage绿 | `#9CBBB3`, `#9CBBA8` |
| 功能色 | 绿/橙/红/蓝 | `#16A34A` / `#EA580C` / `#DC2626` / `#2563EB` |

### 布局结构
- **认证页**(未登录): `.auth-layout` 渐变紫背景 + `.auth-card` 居中卡片
- **应用页**(已登录): `.sidebar`(250px 深青) + `.topbar`(64px) + `.main-content` > `.page-content`
- **移动端**(<768px): 侧边栏滑出式, overlay遮罩, Alpine.js控制

## 业务流程

### 通知发布与已读追踪
```
班长/团支书发布通知(标题+内容+截止时间) → 同班学生查看通知详情 → 自动标记已读
→ 发布人可查看已读/未读名单, 对未读成员提醒
```

### 个人信息变更流程
```
学生/班长编辑个人信息 → 普通学生生成 MemberChangeRecord(待审核)
                      → 班长直接生效(跳审核)
班长审核 → 通过: 更新User字段 + 记录变更 / 驳回: 记录驳回
```

### 推优评议全流程
```
团支书创建推优任务(报名中) → 学生报名(待审核) → 团支书审核(通过/驳回)
→ 手动切换投票阶段 → 学生投票 → 查看结果(得票排名)
```

### 考勤管理流程
```
团支书创建考勤任务(AttendanceTask) → 团支书录入考勤记录(出勤/缺勤/请假)
→ 学生查看自己的考勤记录
学生提交请假申请 → 团支书审核(通过/驳回+意见) → 请假通过后考勤记录自动体现
```

### 党团员管理流程
```
学生上传党团资料 → 团支书审核(通过/驳回+意见)
团支书直接编辑党团员档案(PartyArchive) → 档案信息即时更新
→ 通过的资料在党团员信息库中体现
```

### 活动签到流程
```
班长创建活动+签到码 → 学生报名 → 活动开始 → 学生输入签到码 → 验证签到
```

### 公示材料收集流程
```
团支书发布公示(开启材料收集) → 学生提交材料 → 团支书审核(通过/驳回)
→ 驳回后可重新提交
```

## 注意事项
- 模型字段使用 `db_column` 映射中文列名, 确保与现有数据库兼容
- 普通学生修改个人信息需要班长审核才能生效(班长/团支书修改直接生效)
- 投票有唯一约束: 同一任务中每人只能投给同一候选人一次
- 签到码由活动发布者设置, 学生需输入正确签到码完成签到
- 每个班级的班长和团支书可互相制衡(班长审核学生变更, 团支书审核请假/推优/资料)
- 模板使用Bootstrap 5.3作为网格基础, 自定义CSS类覆盖视觉样式
