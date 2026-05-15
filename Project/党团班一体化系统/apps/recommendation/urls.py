from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("create/", views.task_create, name="task_create"),
    path("<int:tid>/", views.task_detail, name="task_detail"),
    path("<int:tid>/register/", views.task_register, name="task_register"),
    path("<int:tid>/review/", views.review_registrations, name="review_registrations"),
    path("<int:tid>/vote/", views.vote, name="vote"),
    path("<int:tid>/results/", views.results, name="results"),
]
