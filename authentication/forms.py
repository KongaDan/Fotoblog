from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        fields=('username','email','first_name','last_name','role')

class UploadProfilePhotoform(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=('profile_photo',)