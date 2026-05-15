from django import forms
from .models import Publicity, PublicitySubmission


class PublicityForm(forms.ModelForm):
    class Meta:
        model = Publicity
        fields = ["title", "content", "need_material", "collection_start", "collection_end"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5}),
            "collection_start": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "collection_end": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class PublicitySubmissionForm(forms.ModelForm):
    class Meta:
        model = PublicitySubmission
        fields = ["material_content", "attachment_path"]
        widgets = {"material_content": forms.Textarea(attrs={"rows": 4})}
