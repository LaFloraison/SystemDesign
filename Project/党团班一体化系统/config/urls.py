from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("accounts/", include("apps.accounts.urls")),
    path("notifications/", include("apps.notifications.urls")),
    path("activities/", include("apps.activities.urls")),
    path("attendance/", include("apps.attendance.urls")),
    path("party/", include("apps.party.urls")),
    path("recommendation/", include("apps.recommendation.urls")),
    path("publicity/", include("apps.publicity.urls")),
]
