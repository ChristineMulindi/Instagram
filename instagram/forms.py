from django import forms
from .models import Profile,Image
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_path', 'bio']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [ 'image','caption']