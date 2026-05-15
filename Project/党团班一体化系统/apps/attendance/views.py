from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AttendanceTask, AttendanceRecord, LeaveRequest
from .forms import AttendanceTaskForm, LeaveRequestForm, LeaveReviewForm
from apps.accounts.models import User
from apps.accounts.utils import role_required


@login_required
def attendance_records_view(request):
    if request.user.role in ["班长", "团支书"]:
        records = AttendanceRecord.objects.filter(
            user__class_name=request.user.class_name
        ).select_related("user", "recorder").order_by("-attendance_date")
    else:
        records = AttendanceRecord.objects.filter(user=request.user).select_related("recorder").order_by("-attendance_date")
    return render(request, "attendance/records.html", {"records": records})


@login_required
@role_required("团支书")
def attendance_task_create(request):
    if request.method == "POST":
        form = AttendanceTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user
            task.save()
            messages.success(request, "考勤任务已创建")
            return redirect("attendance_records")
    else:
        form = AttendanceTaskForm()
    return render(request, "attendance/task_create.html", {"form": form})


@login_required
@role_required("团支书")
def attendance_record_input(request, tid):
    task = get_object_or_404(AttendanceTask, id=tid)
    classmates = User.objects.filter(class_name=request.user.class_name)
    if request.method == "POST":
        for classmate in classmates:
            status_key = f"status_{classmate.id}"
            if status_key in request.POST:
                AttendanceRecord.objects.update_or_create(
                    attendance_date=task.attendance_time.date(),
                    user=classmate,
                    defaults={
                        "status": request.POST[status_key],
                        "remark": request.POST.get(f"remark_{classmate.id}", ""),
                        "recorder": request.user,
                    },
                )
        messages.success(request, "考勤记录已保存")
        return redirect("attendance_records")
    existing = {r.user_id: r for r in AttendanceRecord.objects.filter(attendance_date=task.attendance_time.date())}
    return render(request, "attendance/record_input.html", {"task": task, "classmates": classmates, "existing": existing})


@login_required
def leave_apply(request):
    if request.method == "POST":
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            messages.success(request, "请假申请已提交，等待审核")
            return redirect("leave_list")
    else:
        form = LeaveRequestForm()
    return render(request, "attendance/leave_apply.html", {"form": form})


@login_required
def leave_list(request):
    if request.user.role in ["班长", "团支书"]:
        leaves = LeaveRequest.objects.filter(user__class_name=request.user.class_name).select_related("user", "reviewer").order_by("-apply_time")
    else:
        leaves = LeaveRequest.objects.filter(user=request.user).select_related("reviewer").order_by("-apply_time")
    return render(request, "attendance/leave_list.html", {"leaves": leaves})


@login_required
@role_required("团支书")
def leave_review(request, lid):
    leave = get_object_or_404(LeaveRequest, id=lid)
    if request.method == "POST":
        form = LeaveReviewForm(request.POST, instance=leave)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.reviewer = request.user
            leave.save()
            messages.success(request, "审核完成")
            return redirect("leave_list")
    else:
        form = LeaveReviewForm(instance=leave)
    return render(request, "attendance/leave_review.html", {"form": form, "leave": leave})
