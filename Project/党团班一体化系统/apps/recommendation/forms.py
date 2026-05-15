from django import forms
from .models import RecommendationTask


class RecommendationTaskForm(forms.ModelForm):
    class Meta:
        model = RecommendationTask
        fields = ["name", "registration_deadline", "vote_start", "vote_end"]
        widgets = {
            "registration_deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "vote_start": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "vote_end": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
