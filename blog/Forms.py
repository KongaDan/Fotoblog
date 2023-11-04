from django import forms
from . import models
from django.conf import settings

class PhotoForm(forms.ModelForm):
    class Meta:
        model=models.Photo
        fields=['image','caption']

class BlogForm(forms.ModelForm):
    class Meta:
        model=models.Blog
        fields=['title','content']