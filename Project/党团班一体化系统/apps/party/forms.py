from django import forms
from .models import PartyMaterialUpload


class PartyMaterialUploadForm(forms.ModelForm):
    class Meta:
        model = PartyMaterialUpload
        fields = ["material_name", "material_path"]


class PartyMaterialReviewForm(forms.ModelForm):
    class Meta:
        model = PartyMaterialUpload
        fields = ["status", "review_comment"]
