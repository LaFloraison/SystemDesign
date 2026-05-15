from django import forms
from .models import Notification


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ["title", "content", "deadline"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5}),
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
