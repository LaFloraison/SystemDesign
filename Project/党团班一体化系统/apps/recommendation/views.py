from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count
from .models import RecommendationTask, RecommendationRegistration, RecommendationVote
from .forms import RecommendationTaskForm
from apps.accounts.utils import role_required


@login_required
def task_list(request):
    tasks = RecommendationTask.objects.all().order_by("-publish_time")
    return render(request, "recommendation/task_list.html", {"tasks": tasks})


@login_required
@role_required("团支书")
def task_create(request):
    if request.method == "POST":
        form = RecommendationTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.publisher = request.user
            task.save()
            messages.success(request, "推优任务已发布")
            return redirect("task_list")
    else:
        form = RecommendationTaskForm()
    return render(request, "recommendation/task_create.html", {"form": form})


@login_required
def task_detail(request, tid):
    task = get_object_or_404(RecommendationTask, id=tid)
    approved = RecommendationRegistration.objects.filter(task=task, status="已通过").select_related("user")
    my_reg = RecommendationRegistration.objects.filter(task=task, user=request.user).first()
    registrations = RecommendationRegistration.objects.filter(task=task).select_related("user")
    votes = RecommendationVote.objects.filter(task=task, voter=request.user)
    voted_ids = set(votes.values_list("candidate_id", flat=True))
    return render(request, "recommendation/task_detail.html", {
        "task": task, "approved": approved, "my_reg": my_reg,
        "registrations": registrations, "voted_ids": voted_ids,
    })


@login_required
def task_register(request, tid):
    task = get_object_or_404(RecommendationTask, id=tid)
    if task.status != "报名中":
        messages.error(request, "当前不在报名阶段")
        return redirect("task_detail", tid=tid)
    if task.registration_deadline and timezone.now() > task.registration_deadline:
        messages.error(request, "报名已截止")
        return redirect("task_detail", tid=tid)
    reg, created = RecommendationRegistration.objects.get_or_create(
        task=task, user=request.user, defaults={"status": "待审核"},
    )
    if created:
        messages.success(request, "报名成功，等待审核")
    else:
        messages.info(request, "已报名")
    return redirect("task_detail", tid=tid)


@login_required
@role_required("团支书")
def review_registrations(request, tid):
    task = get_object_or_404(RecommendationTask, id=tid)
    registrations = RecommendationRegistration.objects.filter(task=task).select_related("user")
    if request.method == "POST":
        reg_id = request.POST.get("reg_id")
        action = request.POST.get("action")
        comment = request.POST.get("review_comment", "")
        reg = get_object_or_404(RecommendationRegistration, id=reg_id)
        reg.status = action
        reg.review_comment = comment
        reg.save()
        messages.success(request, "审核完成")
        return redirect("review_registrations", tid=tid)
    return render(request, "recommendation/review.html", {"task": task, "registrations": registrations})


@login_required
def vote(request, tid):
    task = get_object_or_404(RecommendationTask, id=tid)
    if task.status != "投票中":
        messages.error(request, "当前不在投票阶段")
        return redirect("task_detail", tid=tid)
    if task.vote_end and timezone.now() > task.vote_end:
        messages.error(request, "投票已结束")
        return redirect("task_detail", tid=tid)
    candidates = RecommendationRegistration.objects.filter(task=task, status="已通过").select_related("user")
    if request.method == "POST":
        candidate_id = request.POST.get("candidate_id")
        if candidate_id:
            _, created = RecommendationVote.objects.get_or_create(
                task=task, voter=request.user, candidate_id=candidate_id,
            )
            if created:
                messages.success(request, "投票成功")
            else:
                messages.info(request, "已投过票")
        return redirect("vote", tid=tid)
    my_votes = RecommendationVote.objects.filter(task=task, voter=request.user).values_list("candidate_id", flat=True)
    return render(request, "recommendation/vote.html", {
        "task": task, "candidates": candidates, "my_votes": set(my_votes),
    })


@login_required
def results(request, tid):
    task = get_object_or_404(RecommendationTask, id=tid)
    results_data = RecommendationVote.objects.filter(task=task).values(
        "candidate__name", "candidate__student_id"
    ).annotate(vote_count=Count("id")).order_by("-vote_count")
    return render(request, "recommendation/results.html", {"task": task, "results": results_data})
