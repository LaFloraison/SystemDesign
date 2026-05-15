from django import forms
from .models import AttendanceTask, AttendanceRecord, LeaveRequest


class AttendanceTaskForm(forms.ModelForm):
    class Meta:
        model = AttendanceTask
        fields = ["name", "attendance_time", "location"]
        widgets = {"attendance_time": forms.DateTimeInput(attrs={"type": "datetime-local"})}


class AttendanceRecordForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ["attendance_date", "user", "status", "remark"]
        widgets = {"attendance_date": forms.DateInput(attrs={"type": "date"})}


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ["leave_date", "reason"]
        widgets = {"leave_date": forms.DateInput(attrs={"type": "date"})}


class LeaveReviewForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ["status", "review_comment"]
