from django.urls import path
from . import views

urlpatterns = [
    path("", views.publicity_list, name="publicity_list"),
    path("create/", views.publicity_create, name="publicity_create"),
    path("<int:pid>/", views.publicity_detail, name="publicity_detail"),
    path("<int:pid>/submit/", views.publicity_submit, name="publicity_submit"),
    path("<int:pid>/review/", views.publicity_review, name="publicity_review"),
]
