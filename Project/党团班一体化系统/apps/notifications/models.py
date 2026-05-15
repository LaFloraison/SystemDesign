from django.db import models
from django.conf import settings


class Notification(models.Model):
    STATUS_CHOICES = [
        ("未发布", "未发布"),
        ("已发布", "已发布"),
        ("已过期", "已过期"),
    ]

    id = models.AutoField(primary_key=True, db_column="通知ID")
    title = models.CharField(max_length=100, db_column="标题")
    content = models.TextField(db_column="内容")
    publish_time = models.DateTimeField(auto_now_add=True, db_column="发布时间")
    deadline = models.DateTimeField(null=True, blank=True, db_column="截止时间")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="已发布", db_column="状态"
    )
    publisher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="用户ID",
        related_name="published_notifications",
    )

    class Meta:
        db_table = "通知"
        verbose_name = "通知"
        verbose_name_plural = verbose_name


class NotificationReadRecord(models.Model):
    READ_STATUS_CHOICES = [
        ("未读", "未读"),
        ("已读", "已读"),
    ]

    id = models.AutoField(primary_key=True, db_column="记录ID")
    notification = models.ForeignKey(
        Notification,
        on_delete=models.RESTRICT,
        db_column="通知ID",
        related_name="read_records",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="notification_reads",
    )
    read_time = models.DateTimeField(null=True, blank=True, db_column="已读时间")
    status = models.CharField(
        max_length=10,
        choices=READ_STATUS_CHOICES,
        default="未读",
        db_column="状态",
    )

    class Meta:
        db_table = "通知已读记录"
        verbose_name = "通知已读记录"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=["notification", "user"],
                name="uk_notice_user",
            )
        ]
