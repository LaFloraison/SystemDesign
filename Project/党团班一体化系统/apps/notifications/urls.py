from django.urls import path
from . import views

urlpatterns = [
    path("", views.notification_list, name="notification_list"),
    path("create/", views.notification_create, name="notification_create"),
    path("<int:nid>/", views.notification_detail, name="notification_detail"),
    path("<int:nid>/status/", views.notification_status, name="notification_status"),
]
