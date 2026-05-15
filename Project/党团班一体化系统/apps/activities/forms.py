from django import forms
from .models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["name", "description", "activity_time", "location", "checkin_code", "checkin_deadline"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "activity_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "checkin_deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class CheckInForm(forms.Form):
    checkin_code = forms.CharField(label="签到码", max_length=50)
