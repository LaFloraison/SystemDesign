from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Publicity, PublicitySubmission
from .forms import PublicityForm, PublicitySubmissionForm
from apps.accounts.utils import role_required


@login_required
def publicity_list(request):
    publicities = Publicity.objects.all().order_by("-publish_time")
    return render(request, "publicity/list.html", {"publicities": publicities})


@login_required
@role_required("团支书")
def publicity_create(request):
    if request.method == "POST":
        form = PublicityForm(request.POST)
        if form.is_valid():
            publicity = form.save(commit=False)
            publicity.publisher = request.user
            publicity.save()
            messages.success(request, "公示已发布")
            return redirect("publicity_list")
    else:
        form = PublicityForm()
    return render(request, "publicity/create.html", {"form": form})


@login_required
def publicity_detail(request, pid):
    publicity = get_object_or_404(Publicity, id=pid)
    my_submission = PublicitySubmission.objects.filter(publicity=publicity, user=request.user).first()
    submissions = None
    if request.user.role in ["班长", "团支书"]:
        submissions = publicity.submissions.select_related("user").all()
    return render(request, "publicity/detail.html", {
        "publicity": publicity, "my_submission": my_submission, "submissions": submissions,
    })


@login_required
def publicity_submit(request, pid):
    publicity = get_object_or_404(Publicity, id=pid)
    if publicity.need_material != "是":
        messages.error(request, "该公示不需要提交材料")
        return redirect("publicity_detail", pid=pid)
    existing = PublicitySubmission.objects.filter(publicity=publicity, user=request.user).first()
    if existing and existing.status == "已通过":
        messages.info(request, "材料已通过审核，无需重复提交")
        return redirect("publicity_detail", pid=pid)
    if request.method == "POST":
        form = PublicitySubmissionForm(request.POST, instance=existing)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.publicity = publicity
            submission.user = request.user
            submission.status = "待审核"
            submission.save()
            messages.success(request, "材料已提交，等待审核")
            return redirect("publicity_detail", pid=pid)
    else:
        form = PublicitySubmissionForm(instance=existing)
    return render(request, "publicity/submit.html", {"form": form, "publicity": publicity})


@login_required
@role_required("团支书")
def publicity_review(request, pid):
    publicity = get_object_or_404(Publicity, id=pid)
    submissions = publicity.submissions.select_related("user").all()
    if request.method == "POST":
        sub_id = request.POST.get("submission_id")
        action = request.POST.get("action")
        comment = request.POST.get("review_comment", "")
        submission = get_object_or_404(PublicitySubmission, id=sub_id)
        submission.status = action
        submission.review_comment = comment
        submission.reviewer = request.user
        submission.review_time = timezone.now()
        submission.save()
        messages.success(request, "审核完成")
        return redirect("publicity_review", pid=pid)
    return render(request, "publicity/review.html", {"publicity": publicity, "submissions": submissions})
