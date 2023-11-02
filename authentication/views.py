from django.shortcuts import render,redirect
from .forms import SignupForm,UploadProfilePhotoform
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.conf import settings

def signup_page(request):
    form=SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,'authentication/signup_page.html',{'form':form})

def upload_profile_photo(request):
    form=UploadProfilePhotoform(instance=request.user)
    if request.method=="POST":
        form=UploadProfilePhotoform(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    return render(request,'authentication/upload_profile_photo.html',{'form':form})