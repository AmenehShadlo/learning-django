from django import forms
from accounts.models import ProfileModel

class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=['user','Gender','Credit']