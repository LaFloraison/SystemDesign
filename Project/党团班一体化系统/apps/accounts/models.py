from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, student_id, password=None, **extra_fields):
        if not student_id:
            raise ValueError("学号不能为空")
        extra_fields.setdefault("username", student_id)
        user = self.model(student_id=student_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "团支书")
        return self.create_user(student_id, password, **extra_fields)


class User(AbstractUser):
    GENDER_CHOICES = [("男", "男"), ("女", "女")]
    POLITICAL_CHOICES = [
        ("群众", "群众"),
        ("团员", "团员"),
        ("预备党员", "预备党员"),
        ("党员", "党员"),
    ]
    ROLE_CHOICES = [
        ("普通学生", "普通学生"),
        ("班长", "班长"),
        ("团支书", "团支书"),
    ]

    id = models.AutoField(primary_key=True, db_column="用户ID")
    student_id = models.CharField(max_length=20, unique=True, db_column="学号")
    name = models.CharField(max_length=10, db_column="姓名")
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, null=True, blank=True, db_column="性别"
    )
    class_name = models.CharField(
        max_length=20, null=True, blank=True, db_column="班级"
    )
    phone = models.CharField(
        max_length=11, unique=True, null=True, blank=True, db_column="手机号"
    )
    political_status = models.CharField(
        max_length=10,
        choices=POLITICAL_CHOICES,
        null=True,
        blank=True,
        db_column="政治面貌",
    )
    enrollment_date = models.DateField(null=True, blank=True, db_column="入学时间")
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="普通学生",
        db_column="角色",
    )

    objects = UserManager()

    USERNAME_FIELD = "student_id"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        db_table = "用户"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.student_id} - {self.name}"


class PartyArchive(models.Model):
    POLITICAL_IDENTITY_CHOICES = [
        ("群众", "群众"),
        ("团员", "团员"),
        ("预备党员", "预备党员"),
        ("党员", "党员"),
    ]
    ORG_STATUS_CHOICES = [
        ("正常", "正常"),
        ("转出", "转出"),
        ("转入", "转入"),
    ]

    id = models.AutoField(primary_key=True, db_column="档案ID")
    user = models.OneToOneField(
        User,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="party_archive",
    )
    political_identity = models.CharField(
        max_length=10, choices=POLITICAL_IDENTITY_CHOICES, db_column="政治身份"
    )
    join_league_date = models.DateField(null=True, blank=True, db_column="入团时间")
    join_party_date = models.DateField(null=True, blank=True, db_column="入党时间")
    full_member_date = models.DateField(null=True, blank=True, db_column="转正时间")
    introducer_name = models.CharField(
        max_length=50, null=True, blank=True, db_column="介绍人姓名"
    )
    org_relation_status = models.CharField(
        max_length=10,
        choices=ORG_STATUS_CHOICES,
        default="正常",
        db_column="组织关系状态",
    )

    class Meta:
        db_table = "党团员档案"
        verbose_name = "党团员档案"
        verbose_name_plural = verbose_name


class MemberChangeRecord(models.Model):
    id = models.AutoField(primary_key=True, db_column="变更ID")
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        db_column="用户ID",
        related_name="member_changes",
    )
    operator = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        db_column="操作人ID",
        related_name="operated_changes",
    )
    change_content = models.CharField(max_length=100, db_column="变更内容")
    change_time = models.DateTimeField(auto_now_add=True, db_column="变更时间")
    before_data = models.CharField(
        max_length=255, null=True, blank=True, db_column="变更前数据"
    )
    after_data = models.CharField(
        max_length=255, null=True, blank=True, db_column="变更后数据"
    )

    class Meta:
        db_table = "成员变更记录"
        verbose_name = "成员变更记录"
        verbose_name_plural = verbose_name
