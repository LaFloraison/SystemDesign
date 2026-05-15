from django.urls import path
from . import views

urlpatterns = [
    path("", views.party_material_list, name="party_material_list"),
    path("upload/", views.party_material_upload, name="party_material_upload"),
    path("review/<int:mid>/", views.party_material_review, name="party_material_review"),
]
