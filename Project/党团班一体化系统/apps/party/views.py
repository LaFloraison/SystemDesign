from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import PartyMaterialUpload
from .forms import PartyMaterialUploadForm, PartyMaterialReviewForm
from apps.accounts.utils import role_required


@login_required
def party_material_list(request):
    if request.user.role in ["班长", "团支书"]:
        uploads = PartyMaterialUpload.objects.filter(
            user__class_name=request.user.class_name
        ).select_related("user", "reviewer").order_by("-upload_time")
    else:
        uploads = PartyMaterialUpload.objects.filter(
            user=request.user
        ).select_related("reviewer").order_by("-upload_time")
    return render(request, "party/material_list.html", {"uploads": uploads})


@login_required
def party_material_upload(request):
    if request.method == "POST":
        form = PartyMaterialUploadForm(request.POST)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            messages.success(request, "资料已上传，等待审核")
            return redirect("party_material_list")
    else:
        form = PartyMaterialUploadForm()
    return render(request, "party/upload.html", {"form": form})


@login_required
@role_required("团支书")
def party_material_review(request, mid):
    material = get_object_or_404(PartyMaterialUpload, id=mid)
    if request.method == "POST":
        form = PartyMaterialReviewForm(request.POST, instance=material)
        if form.is_valid():
            material = form.save(commit=False)
            material.reviewer = request.user
            material.review_time = timezone.now()
            material.save()
            messages.success(request, "审核完成")
            return redirect("party_material_list")
    else:
        form = PartyMaterialReviewForm(instance=material)
    return render(request, "party/review.html", {"form": form, "material": material})
