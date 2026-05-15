from django.db import models
from django.conf import settings


class AttendanceTask(models.Model):
    id = models.AutoField(primary_key=True, db_column="考勤ID")
    name = models.CharField(max_length=100, db_column="考勤名称")
    attendance_time = models.DateTimeField(db_column="考勤时间")
    location = models.CharField(
        max_length=100, null=True, blank=True, db_column="考勤地点"
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="用户ID",
        related_name="created_attendance_tasks",
    )

    class Meta:
        db_table = "考勤任务"
        verbose_name = "考勤任务"
        verbose_name_plural = verbose_name


class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ("出勤", "出勤"),
        ("缺勤", "缺勤"),
        ("请假", "请假"),
    ]

    id = models.AutoField(primary_key=True, db_column="记录ID")
    attendance_date = models.DateField(db_column="考勤日期")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="attendance_records",
    )
    recorder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="录入人ID",
        related_name="recorded_attendances",
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, db_column="考勤状态"
    )
    remark = models.CharField(
        max_length=255, null=True, blank=True, db_column="备注"
    )

    class Meta:
        db_table = "考勤记录"
        verbose_name = "考勤记录"
        verbose_name_plural = verbose_name


class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ("待审核", "待审核"),
        ("已通过", "已通过"),
        ("已驳回", "已驳回"),
    ]

    id = models.AutoField(primary_key=True, db_column="申请ID")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="leave_requests",
    )
    leave_date = models.DateField(db_column="请假日期")
    reason = models.CharField(max_length=255, db_column="请假原因")
    apply_time = models.DateTimeField(auto_now_add=True, db_column="申请时间")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="待审核", db_column="审核状态"
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        db_column="审核人ID",
        related_name="reviewed_leaves",
    )
    review_comment = models.CharField(
        max_length=255, null=True, blank=True, db_column="审核意见"
    )

    class Meta:
        db_table = "请假申请"
        verbose_name = "请假申请"
        verbose_name_plural = verbose_name
