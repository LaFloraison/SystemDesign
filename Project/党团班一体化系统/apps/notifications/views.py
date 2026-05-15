from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Notification, NotificationReadRecord
from .forms import NotificationForm
from apps.accounts.utils import role_required


@login_required
def notification_list(request):
    notifications = Notification.objects.filter(
        status="已发布"
    ).order_by("-publish_time")
    return render(request, "notifications/list.html", {"notifications": notifications})


@login_required
@role_required("班长", "团支书")
def notification_create(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.publisher = request.user
            notification.save()
            messages.success(request, "通知已发布")
            return redirect("notification_list")
    else:
        form = NotificationForm()
    return render(request, "notifications/create.html", {"form": form})


@login_required
def notification_detail(request, nid):
    notification = get_object_or_404(Notification, id=nid)
    record, _ = NotificationReadRecord.objects.get_or_create(
        notification=notification,
        user=request.user,
        defaults={"status": "已读", "read_time": timezone.now()},
    )
    if record.status == "未读":
        record.status = "已读"
        record.read_time = timezone.now()
        record.save()
    return render(request, "notifications/detail.html", {"notification": notification})


@login_required
@role_required("班长", "团支书")
def notification_status(request, nid):
    notification = get_object_or_404(Notification, id=nid)
    records = NotificationReadRecord.objects.filter(
        notification=notification
    ).select_related("user")
    return render(request, "notifications/read_status.html", {
        "notification": notification,
        "records": records,
    })
