from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Activity, ActivityRegistration, ActivityCheckIn
from .forms import ActivityForm, CheckInForm
from apps.accounts.utils import role_required


@login_required
def activity_list(request):
    activities = Activity.objects.all().order_by("-activity_time")
    return render(request, "activities/list.html", {"activities": activities})


@login_required
@role_required("班长", "团支书")
def activity_create(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.publisher = request.user
            activity.save()
            messages.success(request, "活动已创建")
            return redirect("activity_list")
    else:
        form = ActivityForm()
    return render(request, "activities/create.html", {"form": form})


@login_required
def activity_detail(request, aid):
    activity = get_object_or_404(Activity, id=aid)
    registration = ActivityRegistration.objects.filter(
        activity=activity, user=request.user
    ).first()
    checkin = ActivityCheckIn.objects.filter(
        activity=activity, user=request.user
    ).first()
    return render(request, "activities/detail.html", {
        "activity": activity, "registration": registration, "checkin": checkin,
    })


@login_required
def activity_register(request, aid):
    activity = get_object_or_404(Activity, id=aid)
    reg, created = ActivityRegistration.objects.get_or_create(
        activity=activity, user=request.user, defaults={"status": "已报名"},
    )
    if not created and reg.status == "已取消":
        reg.status = "已报名"; reg.save()
        messages.success(request, "已重新报名")
    elif created:
        messages.success(request, "报名成功")
    else:
        messages.info(request, "已报名")
    return redirect("activity_detail", aid=aid)


@login_required
def activity_unregister(request, aid):
    activity = get_object_or_404(Activity, id=aid)
    reg = ActivityRegistration.objects.filter(
        activity=activity, user=request.user, status="已报名"
    ).first()
    if reg:
        reg.status = "已取消"; reg.save()
        messages.success(request, "已取消报名")
    return redirect("activity_detail", aid=aid)


@login_required
def activity_checkin(request, aid):
    activity = get_object_or_404(Activity, id=aid)
    if request.method == "POST":
        form = CheckInForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["checkin_code"] != activity.checkin_code:
                messages.error(request, "签到码错误")
                return redirect("activity_detail", aid=aid)
            if activity.checkin_deadline and timezone.now() > activity.checkin_deadline:
                messages.error(request, "签到已截止")
                return redirect("activity_detail", aid=aid)
            checkin, created = ActivityCheckIn.objects.get_or_create(
                activity=activity, user=request.user,
                defaults={"status": "已签到", "checkin_time": timezone.now()},
            )
            if not created and checkin.status == "未签到":
                checkin.status = "已签到"; checkin.checkin_time = timezone.now(); checkin.save()
            messages.success(request, "签到成功")
            return redirect("activity_detail", aid=aid)
    else:
        form = CheckInForm()
    return render(request, "activities/checkin.html", {"form": form, "activity": activity})


@login_required
@role_required("班长", "团支书")
def activity_manage(request, aid):
    activity = get_object_or_404(Activity, id=aid)
    registrations = activity.registrations.filter(status="已报名").select_related("user")
    checkins = activity.checkins.filter(status="已签到").select_related("user")
    return render(request, "activities/manage.html", {
        "activity": activity, "registrations": registrations, "checkins": checkins,
    })
