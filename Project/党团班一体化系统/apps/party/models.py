from django.db import models
from django.conf import settings


class PartyMaterialUpload(models.Model):
    STATUS_CHOICES = [
        ("待审核", "待审核"),
        ("已通过", "已通过"),
        ("已驳回", "已驳回"),
    ]

    id = models.AutoField(primary_key=True, db_column="记录ID")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="party_material_uploads",
    )
    material_name = models.CharField(max_length=100, db_column="资料名称")
    material_path = models.CharField(max_length=255, db_column="资料路径")
    upload_time = models.DateTimeField(auto_now_add=True, db_column="上传时间")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="待审核", db_column="审核状态"
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        db_column="审核人ID",
        related_name="reviewed_party_materials",
    )
    review_time = models.DateTimeField(null=True, blank=True, db_column="审核时间")
    review_comment = models.TextField(null=True, blank=True, db_column="审核意见")

    class Meta:
        db_table = "党团资料上传记录"
        verbose_name = "党团资料上传记录"
        verbose_name_plural = verbose_name


class ProofMaterial(models.Model):
    STATUS_CHOICES = [
        ("待审核", "待审核"),
        ("通过", "通过"),
        ("驳回", "驳回"),
    ]

    id = models.AutoField(primary_key=True, db_column="材料ID")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="用户ID",
        related_name="proof_materials",
    )
    material_name = models.CharField(max_length=100, db_column="材料名称")
    upload_time = models.DateTimeField(auto_now_add=True, db_column="上传时间")
    material_path = models.CharField(max_length=255, db_column="材料路径")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="待审核", db_column="审核状态"
    )

    class Meta:
        db_table = "证明材料"
        verbose_name = "证明材料"
        verbose_name_plural = verbose_name
