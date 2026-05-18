# 党团班一体化系统 - 数据库设计文档

> 18张表, MySQL 8.0, utf8mb4, InnoDB

---

## 1. ER 关系图 (文本)

```
                                    ┌─────────────────┐
                                    │      用 户       │
                                    │  (User)          │
                                    │─────────────────│
                                    │ PK: 用户ID        │
                                    │ UN: 学号, 手机号   │
                                    └──────┬──────────┘
                           ┌───────────────┼───────────────┬───────────────┬───────────────┐
                           │1:1            │1:N            │1:N            │1:N            │1:N
              ┌────────────▼──┐  ┌─────────▼──┐  ┌─────────▼──┐  ┌─────────▼──┐  ┌─────────▼──┐
              │  党团员档案     │  │ 成员变更记录  │  │ 请假申请     │  │ 党团资料     │  │  证明材料    │
              │ PartyArchive  │  │MemberChange │  │LeaveRequest │  │  上传记录     │  │ProofMaterial│
              └───────────────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────────────┘
                                        │                 │               │
                                    操作用户 FK         审核人 FK        审核人 FK

    ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
    │     通 知        │     │     活 动        │     │   考勤任务       │
    │ Notification    │     │   Activity      │     │AttendanceTask  │
    │─────────────────│     │─────────────────│     │─────────────────│
    │ PK: 通知ID       │     │ PK: 活动ID       │     │ PK: 考勤ID       │
    │ FK: 用户ID(发布人)│     │ FK: 用户ID(发布人)│     │ FK: 用户ID(创建人)│
    └───────┬─────────┘     └───────┬─────────┘     └─────────────────┘
            │1:N                    │1:N
   ┌────────▼──────────┐  ┌────────┴──────────┐
   │  通知已读记录       │  │   活动报名记录      │─────┐
   │NotifReadRecord   │  │ActivityRegistrat. │     │1:N
   │──────────────────│  │───────────────────│  ┌──▼──────────┐
   │ FK: 通知ID, 用户ID │  │ FK: 活动ID, 用户ID │  │ 活动签到记录  │
   └──────────────────┘  └───────────────────┘  │ActivityCheck│
                                                 │   In        │
    ┌─────────────────┐                          │FK:活动ID,用户│
    │   推优任务        │                          └─────────────┘
    │RecommendTask    │
    │─────────────────│     ┌─────────────────┐
    │ PK: 任务ID       │     │     公 示        │
    │ FK: 用户ID(发布人)│     │   Publicity     │
    └───────┬─────────┘     │─────────────────│
            │1:N            │ PK: 公示ID       │
   ┌────────┴──────────┐    │ FK: 用户ID(发布人)│
   │   推优报名          │    └───────┬─────────┘
   │RecommendRegist.   │            │1:N
   │──────────────────│   ┌────────▼──────────┐
   │ FK: 任务ID, 用户ID │   │  公示材料提交记录   │
   └──────────────────┘   │PublicitySubmission│
            │1:N           │──────────────────│
   ┌────────▼──────────┐   │FK:公示ID,用户,审核人│
   │  推优投票记录       │   └──────────────────┘
   │RecommendVote      │
   │──────────────────│
   │FK:任务,投票人,候选人│           ┌─────────────────┐
   └──────────────────┘           │   考勤记录        │
                                  │AttendanceRecord │
                                  │─────────────────│
                                  │FK: 用户, 录入人    │
                                  └─────────────────┘
```

---

## 2. 表详细定义

### 2.1 用户 (User) — `apps/accounts/models.py`

Django自定义AbstractUser, `USERNAME_FIELD = 'student_id'`.

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 用户ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 学号 | `student_id` | VARCHAR(20) | UNIQUE, NOT NULL | - | 登录凭证 |
| 姓名 | `name` | VARCHAR(10) | NOT NULL | - | - |
| 性别 | `gender` | CHAR(2) | NULL | - | 男/女 |
| 班级 | `class_name` | VARCHAR(20) | NULL | - | 如 计算机2201 |
| 手机号 | `phone` | VARCHAR(11) | UNIQUE, NULL | - | - |
| 政治面貌 | `political_status` | VARCHAR(10) | NULL | - | 群众/团员/预备党员/党员 |
| 入学时间 | `enrollment_date` | DATE | NULL | - | - |
| 角色 | `role` | VARCHAR(10) | NOT NULL | 普通学生 | 普通学生/班长/团支书 |
| 密码 | `password` | VARCHAR(128) | NOT NULL | - | Django哈希 |
| 用户名 | `username` | VARCHAR(150) | UNIQUE | =student_id | Django继承字段 |
| 邮箱 | `email` | VARCHAR(254) | - | - | Django继承字段 |

**关联关系:**
- 1:1 → 党团员档案 (PartyArchive.user)
- 1:N → 成员变更记录 (MemberChangeRecord.user, MemberChangeRecord.operator)
- 1:N → 通知 (Notification.publisher)
- 1:N → 通知已读记录 (NotificationReadRecord.user)
- 1:N → 活动 (Activity.publisher)
- 1:N → 活动报名记录 (ActivityRegistration.user)
- 1:N → 活动签到记录 (ActivityCheckIn.user)
- 1:N → 考勤任务 (AttendanceTask.creator)
- 1:N → 考勤记录 (AttendanceRecord.user, AttendanceRecord.recorder)
- 1:N → 请假申请 (LeaveRequest.user, LeaveRequest.reviewer)
- 1:N → 党团资料上传记录 (PartyMaterialUpload.user, PartyMaterialUpload.reviewer)
- 1:N → 证明材料 (ProofMaterial.user)
- 1:N → 推优任务 (RecommendationTask.publisher)
- 1:N → 推优报名 (RecommendationRegistration.user)
- 1:N → 推优投票记录 (RecommendationVote.voter, RecommendationVote.candidate)
- 1:N → 公示 (Publicity.publisher)
- 1:N → 公示材料提交记录 (PublicitySubmission.user, PublicitySubmission.reviewer)

---

### 2.2 党团员档案 (PartyArchive) — `apps/accounts/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 档案ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 用户ID | `user_id` | INT | UNIQUE, FK→用户, RESTRICT | - | 一对一 |
| 政治身份 | `political_identity` | VARCHAR(10) | NOT NULL | - | 群众/团员/预备党员/党员 |
| 入团时间 | `join_league_date` | DATE | NULL | - | - |
| 入党时间 | `join_party_date` | DATE | NULL | - | - |
| 转正时间 | `full_member_date` | DATE | NULL | - | - |
| 介绍人姓名 | `introducer_name` | VARCHAR(50) | NULL | - | - |
| 组织关系状态 | `org_relation_status` | VARCHAR(10) | NULL | 正常 | 正常/转出/转入 |

---

### 2.3 成员变更记录 (MemberChangeRecord) — `apps/accounts/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 变更ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | 被修改人 |
| 操作人ID | `operator_id` | INT | FK→用户, RESTRICT | - | 修改发起人或审核人 |
| 变更内容 | `change_content` | VARCHAR(100) | NOT NULL | - | 如"修改个人信息" |
| 变更时间 | `change_time` | DATETIME | - | auto_now_add | - |
| 变更前数据 | `before_data` | VARCHAR(255) | NULL | - | JSON格式 |
| 变更后数据 | `after_data` | VARCHAR(255) | NULL | - | JSON格式 |

**业务规则:** 普通学生修改信息生成记录(待审核); 班长审核通过/驳回; 班长/团支书修改直接生效不生成待审核记录

---

### 2.4 通知 (Notification) — `apps/notifications/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 通知ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 标题 | `title` | VARCHAR(100) | NOT NULL | - | - |
| 内容 | `content` | TEXT | NOT NULL | - | - |
| 发布时间 | `publish_time` | DATETIME | - | auto_now_add | - |
| 截止时间 | `deadline` | DATETIME | NULL | - | - |
| 状态 | `status` | VARCHAR(10) | NOT NULL | 已发布 | 未发布/已发布/已过期 |
| 用户ID | `publisher_id` | INT | FK→用户, CASCADE | - | 发布人 |

---

### 2.5 通知已读记录 (NotificationReadRecord) — `apps/notifications/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 记录ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 通知ID | `notification_id` | INT | FK→通知, RESTRICT | - | - |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | - |
| 已读时间 | `read_time` | DATETIME | NULL | - | - |
| 状态 | `status` | VARCHAR(10) | NULL | 未读 | 未读/已读 |

**唯一约束:** `(通知ID, 用户ID)` — 每人每条通知只有一条记录

---

### 2.6 活动 (Activity) — `apps/activities/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 活动ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 活动名称 | `name` | VARCHAR(100) | NOT NULL | - | - |
| 活动描述 | `description` | TEXT | NULL | - | - |
| 活动时间 | `activity_time` | DATETIME | NOT NULL | - | - |
| 活动地点 | `location` | VARCHAR(100) | NULL | - | - |
| 发布人ID | `publisher_id` | INT | FK→用户, RESTRICT | - | - |
| 发布时间 | `publish_time` | DATETIME | - | auto_now_add | - |
| 签到码 | `checkin_code` | VARCHAR(50) | NULL | - | 学生签到用 |
| 签到截止时间 | `checkin_deadline` | DATETIME | NULL | - | - |
| 状态 | `status` | VARCHAR(10) | NOT NULL | 报名中 | 报名中/进行中/已结束 |

---

### 2.7 活动报名记录 (ActivityRegistration) — `apps/activities/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 报名ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 活动ID | `activity_id` | INT | FK→活动, RESTRICT | - | - |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | - |
| 报名时间 | `registration_time` | DATETIME | - | auto_now_add | - |
| 报名状态 | `status` | VARCHAR(10) | NOT NULL | 已报名 | 已报名/已取消 |

**唯一约束:** `(活动ID, 用户ID)`

---

### 2.8 活动签到记录 (ActivityCheckIn) — `apps/activities/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 签到ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 活动ID | `activity_id` | INT | FK→活动, RESTRICT | - | - |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | - |
| 签到时间 | `checkin_time` | DATETIME | NULL | - | - |
| 签到状态 | `status` | VARCHAR(10) | NULL | 未签到 | 已签到/未签到 |

**唯一约束:** `(活动ID, 用户ID)`

---

### 2.9 考勤任务 (AttendanceTask) — `apps/attendance/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 考勤ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 考勤名称 | `name` | VARCHAR(100) | NOT NULL | - | - |
| 考勤时间 | `attendance_time` | DATETIME | NOT NULL | - | - |
| 考勤地点 | `location` | VARCHAR(100) | NULL | - | - |
| 用户ID | `creator_id` | INT | FK→用户, CASCADE | - | 创建人(团支书) |

---

### 2.10 考勤记录 (AttendanceRecord) — `apps/attendance/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 记录ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 考勤日期 | `attendance_date` | DATE | NOT NULL | - | - |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | 被考勤学生 |
| 录入人ID | `recorder_id` | INT | FK→用户, RESTRICT | - | 录入人(团支书) |
| 考勤状态 | `status` | VARCHAR(10) | NOT NULL | - | 出勤/缺勤/请假 |
| 备注 | `remark` | VARCHAR(255) | NULL | - | - |

---

### 2.11 请假申请 (LeaveRequest) — `apps/attendance/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 申请ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | 申请人 |
| 请假日期 | `leave_date` | DATE | NOT NULL | - | - |
| 请假原因 | `reason` | VARCHAR(255) | NOT NULL | - | - |
| 申请时间 | `apply_time` | DATETIME | - | auto_now_add | - |
| 审核状态 | `status` | VARCHAR(10) | NOT NULL | 待审核 | 待审核/已通过/已驳回 |
| 审核人ID | `reviewer_id` | INT | FK→用户, RESTRICT, NULL | - | 团支书 |
| 审核意见 | `review_comment` | VARCHAR(255) | NULL | - | - |

---

### 2.12 党团资料上传记录 (PartyMaterialUpload) — `apps/party/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 记录ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | 上传人 |
| 资料名称 | `material_name` | VARCHAR(100) | NOT NULL | - | - |
| 资料路径 | `material_path` | VARCHAR(255) | NOT NULL | - | 文件存储路径 |
| 上传时间 | `upload_time` | DATETIME | - | auto_now_add | - |
| 审核状态 | `status` | VARCHAR(10) | NOT NULL | 待审核 | 待审核/已通过/已驳回 |
| 审核人ID | `reviewer_id` | INT | FK→用户, RESTRICT, NULL | - | 团支书 |
| 审核时间 | `review_time` | DATETIME | NULL | - | - |
| 审核意见 | `review_comment` | TEXT | NULL | - | - |

---

### 2.13 证明材料 (ProofMaterial) — `apps/party/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 材料ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 用户ID | `user_id` | INT | FK→用户, CASCADE | - | 上传人 |
| 材料名称 | `material_name` | VARCHAR(100) | NOT NULL | - | - |
| 上传时间 | `upload_time` | DATETIME | NOT NULL | auto_now_add | - |
| 材料路径 | `material_path` | VARCHAR(255) | NOT NULL | - | - |
| 审核状态 | `status` | VARCHAR(10) | NOT NULL | 待审核 | 待审核/通过/驳回 |

---

### 2.14 推优任务 (RecommendationTask) — `apps/recommendation/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 任务ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 任务名称 | `name` | VARCHAR(100) | NOT NULL | - | - |
| 发布人ID | `publisher_id` | INT | FK→用户, RESTRICT | - | 团支书 |
| 发布时间 | `publish_time` | DATETIME | - | auto_now_add | - |
| 报名截止时间 | `registration_deadline` | DATETIME | NULL | - | - |
| 投票开始时间 | `vote_start` | DATETIME | NULL | - | - |
| 投票结束时间 | `vote_end` | DATETIME | NULL | - | - |
| 状态 | `status` | VARCHAR(10) | NOT NULL | 报名中 | 报名中/投票中/已结束 |

**业务规则:** 团支书手动切换状态(报名中→投票中→已结束), 系统不自动切换

---

### 2.15 推优报名 (RecommendationRegistration) — `apps/recommendation/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 报名ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 任务ID | `task_id` | INT | FK→推优任务, RESTRICT | - | - |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | 报名人 |
| 报名时间 | `registration_time` | DATETIME | - | auto_now_add | - |
| 审核状态 | `status` | VARCHAR(10) | NOT NULL | 待审核 | 待审核/已通过/已驳回 |
| 审核意见 | `review_comment` | TEXT | NULL | - | - |

**唯一约束:** `(任务ID, 用户ID)` — 每人每任务只能报名一次

---

### 2.16 推优投票记录 (RecommendationVote) — `apps/recommendation/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 投票ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 任务ID | `task_id` | INT | FK→推优任务, RESTRICT | - | - |
| 投票人ID | `voter_id` | INT | FK→用户, RESTRICT | - | - |
| 被投票人ID | `candidate_id` | INT | FK→用户, RESTRICT | - | 候选人 |
| 投票时间 | `vote_time` | DATETIME | - | auto_now_add | - |

**唯一约束:** `(任务ID, 投票人ID, 被投票人ID)` — 同一任务中不能重复投给同一个人

---

### 2.17 公示 (Publicity) — `apps/publicity/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 公示ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 标题 | `title` | VARCHAR(100) | NOT NULL | - | - |
| 内容 | `content` | TEXT | NOT NULL | - | - |
| 发布人ID | `publisher_id` | INT | FK→用户, RESTRICT | - | 团支书 |
| 发布时间 | `publish_time` | DATETIME | - | auto_now_add | - |
| 材料收集开始 | `collection_start` | DATETIME | NULL | - | - |
| 材料收集截止 | `collection_end` | DATETIME | NULL | - | - |
| 是否需要提交材料 | `need_material` | VARCHAR(2) | NOT NULL | 否 | 是/否 |
| 状态 | `status` | VARCHAR(10) | NOT NULL | 进行中 | 进行中/已结束 |

---

### 2.18 公示材料提交记录 (PublicitySubmission) — `apps/publicity/models.py`

| 列名 | 字段 | 类型 | 约束 | 默认值 | 说明 |
|---|---|---|---|---|---|
| 提交ID | `id` | INT AUTO_INCREMENT | PK | - | 主键 |
| 公示ID | `publicity_id` | INT | FK→公示, RESTRICT | - | - |
| 用户ID | `user_id` | INT | FK→用户, RESTRICT | - | 提交人 |
| 材料内容 | `material_content` | TEXT | NULL | - | - |
| 材料附件路径 | `attachment_path` | VARCHAR(255) | NULL | - | - |
| 提交时间 | `submit_time` | DATETIME | - | auto_now_add | - |
| 审核状态 | `status` | VARCHAR(10) | NOT NULL | 待审核 | 待审核/已通过/已驳回 |
| 审核人ID | `reviewer_id` | INT | FK→用户, RESTRICT, NULL | - | 团支书 |
| 审核时间 | `review_time` | DATETIME | NULL | - | - |
| 审核意见 | `review_comment` | TEXT | NULL | - | - |

**唯一约束:** `(公示ID, 用户ID)` — 每人每次公示只能提交一次材料; 驳回后可重新提交(覆盖)

---

## 3. 外键删除规则汇总

| 表 | 外键 | ON DELETE |
|---|---|---|
| 党团员档案 | `user` | RESTRICT |
| 成员变更记录 | `user`, `operator` | RESTRICT |
| 通知 | `publisher` | CASCADE |
| 通知已读记录 | `notification`, `user` | RESTRICT |
| 活动 | `publisher` | RESTRICT |
| 活动报名记录 | `activity`, `user` | RESTRICT |
| 活动签到记录 | `activity`, `user` | RESTRICT |
| 考勤任务 | `creator` | CASCADE |
| 考勤记录 | `user`, `recorder` | RESTRICT |
| 请假申请 | `user`, `reviewer` | RESTRICT |
| 党团资料上传记录 | `user`, `reviewer` | RESTRICT |
| 证明材料 | `user` | CASCADE |
| 推优任务 | `publisher` | RESTRICT |
| 推优报名 | `task`, `user` | RESTRICT |
| 推优投票记录 | `task`, `voter`, `candidate` | RESTRICT |
| 公示 | `publisher` | RESTRICT |
| 公示材料提交记录 | `publicity`, `user`, `reviewer` | RESTRICT |

**规则说明:**
- `RESTRICT`: 有关联数据时禁止删除用户/任务等 (防止误删)
- `CASCADE`: 删除通知/考勤任务/用户时, 自动清除关联记录

---

## 4. 唯一约束汇总

| 约束名 | 表 | 字段 |
|---|---|---|
| - (Django) | 党团员档案 | `user` |
| - (Django) | 用户 | `student_id`, `phone` |
| `uk_notice_user` | 通知已读记录 | `notification`, `user` |
| `uk_activity_user` | 活动报名记录 | `activity`, `user` |
| `uk_activity_sign` | 活动签到记录 | `activity`, `user` |
| `uk_task_user` | 推优报名 | `task`, `user` |
| `uk_task_voter` | 推优投票记录 | `task`, `voter`, `candidate` |
| `uk_publicity_user` | 公示材料提交记录 | `publicity`, `user` |

---

## 5. 状态字段枚举值

| 表 | 字段 | 可选值 |
|---|---|---|
| 用户 | `role` | 普通学生, 班长, 团支书 |
| 用户 | `political_status` | 群众, 团员, 预备党员, 党员 |
| 用户 | `gender` | 男, 女 |
| 党团员档案 | `political_identity` | 群众, 团员, 预备党员, 党员 |
| 党团员档案 | `org_relation_status` | 正常, 转出, 转入 |
| 通知 | `status` | 未发布, 已发布, 已过期 |
| 通知已读记录 | `status` | 未读, 已读 |
| 活动 | `status` | 报名中, 进行中, 已结束 |
| 活动报名记录 | `status` | 已报名, 已取消 |
| 活动签到记录 | `status` | 已签到, 未签到 |
| 考勤记录 | `status` | 出勤, 缺勤, 请假 |
| 请假申请 | `status` | 待审核, 已通过, 已驳回 |
| 党团资料上传记录 | `status` | 待审核, 已通过, 已驳回 |
| 证明材料 | `status` | 待审核, 通过, 驳回 |
| 推优任务 | `status` | 报名中, 投票中, 已结束 |
| 推优报名 | `status` | 待审核, 已通过, 已驳回 |
| 公示 | `need_material` | 是, 否 |
| 公示 | `status` | 进行中, 已结束 |
| 公示材料提交记录 | `status` | 待审核, 已通过, 已驳回 |
