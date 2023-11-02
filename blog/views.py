from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Photo
from . import Forms

@login_required
def home(request):
    photos=Photo.objects.all()
    return render(request,'blog/home.html',{'photos':photos})

@login_required
def photo_upload(request):
    form=Forms.PhotoForm()
    if request.method =="POST":
        form=Forms.PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.uploader=request.user
            photo.save()
            return redirect('blog:home')
    return render(request,'blog/photo_upload.html',{'form':form})