# 党团班一体化系统

基于 Django 的党团班一体化管理系统，服务于高校班级的日常管理。

## 功能模块

| 模块 | 说明 |
|---|---|
| 用户认证 | 学号+密码登录/注册, 三角色(学生/班长/团支书) |
| 个人信息管理 | 查看/编辑个人资料, 班长审核成员变更, 团支书管理党团员档案 |
| 通知管理 | 班长/团支书发布通知, 学生查看, 已读追踪 |
| 活动管理 | 创建活动, 报名/取消, 签到码签到 |
| 考勤管理 | 考勤任务, 考勤记录录入, 请假申请与审核 |
| 党团员管理 | 上传党团资料, 团支书审核, 党团员档案编辑 |
| 推优评议 | 推优任务, 报名审核, 投票, 结果展示 |
| 公示管理 | 发布公示, 材料提交, 审核反馈 |

## 快速开始

```bash
# 1. 环境
conda activate djangoDev
cd "D:\ProjectBase\SystemDesign\Project\党团班一体化系统"
pip install -r requirements.txt

# 2. 配置 .env (数据库连接)
cp .env .env.example  # 编辑 .env 填入MySQL密码

# 3. 迁移 + 种子数据
python manage.py migrate
python manage.py seed_data

# 4. 启动
python manage.py runserver
# 访问 http://localhost:8000
```

## 默认账号 (50个)

| 班级 | 学号范围 | 默认密码 |
|---|---|---|
| 计算机2201 | 20240001 ~ 20240025 | `123456` |
| 计算机2202 | 20240026 ~ 20240050 | `123456` |

每班第1人为班长, 第2人为团支书, 其余为学生。

## 技术栈

- **后端:** Django 6.0
- **数据库:** MySQL 8.0 (utf8mb4)
- **前端:** Django Templates + Bootstrap 5.3 + 自定义CSS
- **图标:** Bootstrap Icons
- **交互:** Alpine.js

## 项目结构

```
├── config/          # settings, urls, wsgi
├── apps/
│   ├── accounts/        # 用户, 党团员档案, 成员变更
│   ├── notifications/   # 通知, 已读记录
│   ├── activities/      # 活动, 报名, 签到
│   ├── attendance/      # 考勤, 请假
│   ├── party/           # 党团资料上传审核
│   ├── recommendation/  # 推优任务, 报名, 投票
│   └── publicity/       # 公示, 材料提交审核
├── templates/       # base.html, home.html
├── static/css/      # design-tokens, components, layout
└── manage.py
```

## 文档

- [系统设计](.claude/CLAUDE.md) — 系统整体设计
- [数据库设计](Project/党团班一体化系统/documents/database_design.md) -数据库详细信息
- [外观设计](Project/党团班一体化系统/documents/ui_design.md) — UI配色/组件/布局规范
- [使用文档](Project/党团班一体化系统/documents/党团班一体化系统.md) — 各角色操作指南

