from django import forms
from . import models
from django.conf import settings
from django.contrib.auth import get_user_model
class PhotoForm(forms.ModelForm):
    class Meta:
        model=models.Photo
        fields=['image','caption']

class BlogForm(forms.ModelForm):
    edit_blog=forms.BooleanField(widget=forms.HiddenInput,initial=True)
    class Meta:
        model=models.Blog
        fields=['title','content']

class DeleteBlogForm(forms.Form):
    delete_blog=forms.BooleanField(widget=forms.HiddenInput,initial=True)

class FolowUserForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=['follows']