from django.db import models
from django.conf import settings


class Publicity(models.Model):
    NEED_MATERIAL_CHOICES = [
        ("是", "是"),
        ("否", "否"),
    ]
    STATUS_CHOICES = [
        ("进行中", "进行中"),
        ("已结束", "已结束"),
    ]

    id = models.AutoField(primary_key=True, db_column="公示ID")
    title = models.CharField(max_length=100, db_column="标题")
    content = models.TextField(db_column="内容")
    publisher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="发布人ID",
        related_name="published_publicities",
    )
    publish_time = models.DateTimeField(auto_now_add=True, db_column="发布时间")
    collection_start = models.DateTimeField(
        null=True, blank=True, db_column="材料收集开始时间"
    )
    collection_end = models.DateTimeField(
        null=True, blank=True, db_column="材料收集截止时间"
    )
    need_material = models.CharField(
        max_length=2,
        choices=NEED_MATERIAL_CHOICES,
        default="否",
        db_column="是否需要提交材料",
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="进行中", db_column="状态"
    )

    class Meta:
        db_table = "公示"
        verbose_name = "公示"
        verbose_name_plural = verbose_name


class PublicitySubmission(models.Model):
    STATUS_CHOICES = [
        ("待审核", "待审核"),
        ("已通过", "已通过"),
        ("已驳回", "已驳回"),
    ]

    id = models.AutoField(primary_key=True, db_column="提交ID")
    publicity = models.ForeignKey(
        Publicity,
        on_delete=models.RESTRICT,
        db_column="公示ID",
        related_name="submissions",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="publicity_submissions",
    )
    material_content = models.TextField(null=True, blank=True, db_column="材料内容")
    attachment_path = models.CharField(
        max_length=255, null=True, blank=True, db_column="材料附件路径"
    )
    submit_time = models.DateTimeField(auto_now_add=True, db_column="提交时间")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="待审核", db_column="审核状态"
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        db_column="审核人ID",
        related_name="reviewed_publicity_submissions",
    )
    review_time = models.DateTimeField(null=True, blank=True, db_column="审核时间")
    review_comment = models.TextField(null=True, blank=True, db_column="审核意见")

    class Meta:
        db_table = "公示材料提交记录"
        verbose_name = "公示材料提交记录"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=["publicity", "user"],
                name="uk_publicity_user",
            )
        ]
