from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_edit_view, name="profile_edit"),
    path("member-changes/", views.member_changes_view, name="member_changes"),
    path("member-changes/<int:change_id>/approve/", views.approve_change, name="approve_change"),
    path("member-changes/<int:change_id>/reject/", views.reject_change, name="reject_change"),
    path("party-archive/", views.party_archive_list_view, name="party_archive_list"),
    path("party-archive/<int:user_id>/edit/", views.party_archive_edit_view, name="party_archive_edit"),
]
