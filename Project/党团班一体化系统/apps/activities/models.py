from django.db import models
from django.conf import settings


class Activity(models.Model):
    STATUS_CHOICES = [
        ("报名中", "报名中"),
        ("进行中", "进行中"),
        ("已结束", "已结束"),
    ]

    id = models.AutoField(primary_key=True, db_column="活动ID")
    name = models.CharField(max_length=100, db_column="活动名称")
    description = models.TextField(null=True, blank=True, db_column="活动描述")
    activity_time = models.DateTimeField(db_column="活动时间")
    location = models.CharField(
        max_length=100, null=True, blank=True, db_column="活动地点"
    )
    publisher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="发布人ID",
        related_name="published_activities",
    )
    publish_time = models.DateTimeField(auto_now_add=True, db_column="发布时间")
    checkin_code = models.CharField(
        max_length=50, null=True, blank=True, db_column="签到码"
    )
    checkin_deadline = models.DateTimeField(
        null=True, blank=True, db_column="签到截止时间"
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="报名中", db_column="状态"
    )

    class Meta:
        db_table = "活动"
        verbose_name = "活动"
        verbose_name_plural = verbose_name


class ActivityRegistration(models.Model):
    STATUS_CHOICES = [
        ("已报名", "已报名"),
        ("已取消", "已取消"),
    ]

    id = models.AutoField(primary_key=True, db_column="报名ID")
    activity = models.ForeignKey(
        Activity,
        on_delete=models.RESTRICT,
        db_column="活动ID",
        related_name="registrations",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="activity_registrations",
    )
    registration_time = models.DateTimeField(auto_now_add=True, db_column="报名时间")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="已报名", db_column="报名状态"
    )

    class Meta:
        db_table = "活动报名记录"
        verbose_name = "活动报名记录"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=["activity", "user"],
                name="uk_activity_user",
            )
        ]


class ActivityCheckIn(models.Model):
    STATUS_CHOICES = [
        ("已签到", "已签到"),
        ("未签到", "未签到"),
    ]

    id = models.AutoField(primary_key=True, db_column="签到ID")
    activity = models.ForeignKey(
        Activity,
        on_delete=models.RESTRICT,
        db_column="活动ID",
        related_name="checkins",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="activity_checkins",
    )
    checkin_time = models.DateTimeField(null=True, blank=True, db_column="签到时间")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="未签到", db_column="签到状态"
    )

    class Meta:
        db_table = "活动签到记录"
        verbose_name = "活动签到记录"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=["activity", "user"],
                name="uk_activity_sign",
            )
        ]
