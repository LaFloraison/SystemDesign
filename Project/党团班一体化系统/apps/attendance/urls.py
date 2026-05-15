from django.urls import path
from . import views

urlpatterns = [
    path("", views.attendance_records_view, name="attendance_records"),
    path("tasks/create/", views.attendance_task_create, name="attendance_task_create"),
    path("tasks/<int:tid>/input/", views.attendance_record_input, name="attendance_record_input"),
    path("leave/apply/", views.leave_apply, name="leave_apply"),
    path("leave/", views.leave_list, name="leave_list"),
    path("leave/<int:lid>/review/", views.leave_review, name="leave_review"),
]
