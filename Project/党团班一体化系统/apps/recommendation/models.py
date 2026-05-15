from django.db import models
from django.conf import settings


class RecommendationTask(models.Model):
    STATUS_CHOICES = [
        ("报名中", "报名中"),
        ("投票中", "投票中"),
        ("已结束", "已结束"),
    ]

    id = models.AutoField(primary_key=True, db_column="任务ID")
    name = models.CharField(max_length=100, db_column="任务名称")
    publisher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="发布人ID",
        related_name="published_recommendations",
    )
    publish_time = models.DateTimeField(auto_now_add=True, db_column="发布时间")
    registration_deadline = models.DateTimeField(
        null=True, blank=True, db_column="报名截止时间"
    )
    vote_start = models.DateTimeField(null=True, blank=True, db_column="投票开始时间")
    vote_end = models.DateTimeField(null=True, blank=True, db_column="投票结束时间")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="报名中", db_column="状态"
    )

    class Meta:
        db_table = "推优任务"
        verbose_name = "推优任务"
        verbose_name_plural = verbose_name


class RecommendationRegistration(models.Model):
    STATUS_CHOICES = [
        ("待审核", "待审核"),
        ("已通过", "已通过"),
        ("已驳回", "已驳回"),
    ]

    id = models.AutoField(primary_key=True, db_column="报名ID")
    task = models.ForeignKey(
        RecommendationTask,
        on_delete=models.RESTRICT,
        db_column="任务ID",
        related_name="registrations",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="recommendation_registrations",
    )
    registration_time = models.DateTimeField(auto_now_add=True, db_column="报名时间")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="待审核", db_column="审核状态"
    )
    review_comment = models.TextField(null=True, blank=True, db_column="审核意见")

    class Meta:
        db_table = "推优报名"
        verbose_name = "推优报名"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=["task", "user"],
                name="uk_task_user",
            )
        ]


class RecommendationVote(models.Model):
    id = models.AutoField(primary_key=True, db_column="投票ID")
    task = models.ForeignKey(
        RecommendationTask,
        on_delete=models.RESTRICT,
        db_column="任务ID",
        related_name="votes",
    )
    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="投票人ID",
        related_name="votes_cast",
    )
    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="被投票人ID",
        related_name="votes_received",
    )
    vote_time = models.DateTimeField(auto_now_add=True, db_column="投票时间")

    class Meta:
        db_table = "推优投票记录"
        verbose_name = "推优投票记录"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=["task", "voter", "candidate"],
                name="uk_task_voter",
            )
        ]
