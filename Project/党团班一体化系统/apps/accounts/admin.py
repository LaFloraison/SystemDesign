from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PartyArchive, MemberChangeRecord


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["student_id", "name", "class_name", "role", "political_status"]
    fieldsets = (
        (None, {"fields": ("student_id", "password")}),
        ("个人信息", {"fields": ("name", "gender", "class_name", "phone")}),
        ("政治信息", {"fields": ("political_status", "enrollment_date", "role")}),
        ("权限", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("student_id", "name", "password1", "password2")}),
    )
    search_fields = ["student_id", "name"]
    ordering = ["student_id"]


@admin.register(PartyArchive)
class PartyArchiveAdmin(admin.ModelAdmin):
    list_display = ["user", "political_identity", "org_relation_status"]


@admin.register(MemberChangeRecord)
class MemberChangeRecordAdmin(admin.ModelAdmin):
    list_display = ["user", "change_content", "change_time"]
