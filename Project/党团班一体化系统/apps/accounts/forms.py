from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, PartyArchive


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="学号", max_length=20)
    password = forms.CharField(label="密码", widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="密码", widget=forms.PasswordInput, min_length=6)
    password_confirm = forms.CharField(label="确认密码", widget=forms.PasswordInput, min_length=6)

    class Meta:
        model = User
        fields = ["student_id", "name", "gender", "class_name", "phone"]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password") != cleaned.get("password_confirm"):
            raise forms.ValidationError("两次输入的密码不一致")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.student_id
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "gender", "phone", "political_status", "class_name", "enrollment_date"]


class PartyArchiveForm(forms.ModelForm):
    class Meta:
        model = PartyArchive
        fields = [
            "political_identity", "join_league_date", "join_party_date",
            "full_member_date", "introducer_name", "org_relation_status",
        ]
