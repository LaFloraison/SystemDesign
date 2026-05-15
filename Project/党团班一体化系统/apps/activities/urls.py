from django.urls import path
from . import views

urlpatterns = [
    path("", views.activity_list, name="activity_list"),
    path("create/", views.activity_create, name="activity_create"),
    path("<int:aid>/", views.activity_detail, name="activity_detail"),
    path("<int:aid>/register/", views.activity_register, name="activity_register"),
    path("<int:aid>/unregister/", views.activity_unregister, name="activity_unregister"),
    path("<int:aid>/checkin/", views.activity_checkin, name="activity_checkin"),
    path("<int:aid>/manage/", views.activity_manage, name="activity_manage"),
]
