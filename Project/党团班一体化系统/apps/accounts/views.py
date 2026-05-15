import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm, ProfileEditForm, PartyArchiveForm
from .models import PartyArchive, MemberChangeRecord
from .utils import role_required


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            PartyArchive.objects.create(
                user=user,
                political_identity=user.political_status or "群众",
            )
            messages.success(request, "注册成功，请登录")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"欢迎回来，{user.name}")
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "已退出登录")
    return redirect("login")


@login_required
def profile_view(request):
    archive = PartyArchive.objects.filter(user=request.user).first()
    changes = MemberChangeRecord.objects.filter(
        user=request.user
    ).order_by("-change_time")[:10]
    return render(request, "accounts/profile.html", {"archive": archive, "changes": changes})


@login_required
def profile_edit_view(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            old_data = json.dumps({
                "name": request.user.name,
                "gender": request.user.gender or "",
                "phone": request.user.phone or "",
                "political_status": request.user.political_status or "",
                "class_name": request.user.class_name or "",
            }, ensure_ascii=False)
            new_data = json.dumps(form.cleaned_data, ensure_ascii=False)

            if request.user.role in ["班长", "团支书"]:
                form.save()
                messages.success(request, "个人信息修改成功")
                return redirect("profile")
            else:
                MemberChangeRecord.objects.create(
                    user=request.user,
                    operator=request.user,
                    change_content="修改个人信息",
                    before_data=old_data,
                    after_data=new_data,
                )
                messages.success(request, "修改申请已提交，等待班长审核")
                return redirect("profile")
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, "accounts/profile_edit.html", {"form": form})


@login_required
@role_required("班长")
def member_changes_view(request):
    changes = MemberChangeRecord.objects.filter(
        user__class_name=request.user.class_name,
    ).order_by("-change_time")
    return render(request, "accounts/member_changes.html", {"changes": changes})


@login_required
@role_required("班长")
def approve_change(request, change_id):
    change = get_object_or_404(MemberChangeRecord, id=change_id)
    if change.user.class_name != request.user.class_name:
        messages.error(request, "无权操作其他班级的变更")
        return redirect("member_changes")
    new_data = json.loads(change.after_data)
    for field, value in new_data.items():
        setattr(change.user, field, value)
    change.user.save()
    MemberChangeRecord.objects.create(
        user=change.user,
        operator=request.user,
        change_content="审核通过: " + change.change_content,
        before_data=change.before_data,
        after_data=change.after_data,
    )
    messages.success(request, "已通过变更申请")
    return redirect("member_changes")


@login_required
@role_required("班长")
def reject_change(request, change_id):
    change = get_object_or_404(MemberChangeRecord, id=change_id)
    MemberChangeRecord.objects.create(
        user=change.user,
        operator=request.user,
        change_content="审核驳回: " + change.change_content,
    )
    messages.success(request, "已驳回变更申请")
    return redirect("member_changes")


@login_required
@role_required("团支书")
def party_archive_list_view(request):
    archives = PartyArchive.objects.filter(
        user__class_name=request.user.class_name
    ).select_related("user")
    return render(request, "accounts/party_archive.html", {"archives": archives})


@login_required
@role_required("团支书")
def party_archive_edit_view(request, user_id):
    archive = get_object_or_404(PartyArchive, user_id=user_id)
    if request.method == "POST":
        form = PartyArchiveForm(request.POST, instance=archive)
        if form.is_valid():
            form.save()
            messages.success(request, "党团员档案已更新")
            return redirect("party_archive_list")
    else:
        form = PartyArchiveForm(instance=archive)
    return render(request, "accounts/party_archive_edit.html", {"form": form, "archive": archive})
