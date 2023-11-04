from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Photo,Blog
from . import Forms

@login_required
def home(request):
    photos=Photo.objects.all()
    blogs=Blog.objects.all()
    return render(request,'blog/home.html',{'photos':photos,'blogs':blogs})

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

@login_required
def blog_add(request):
    blog_form=Forms.BlogForm()
    photo_form=Forms.PhotoForm()
    if request.method=="POST":
        blog_form=Forms.BlogForm(request.POST)
        photo_form=Forms.PhotoForm(request.POST,request.FILES)
        if all([blog_form.is_valid(),photo_form.is_valid()]):
            photo=photo_form.save(commit=False)
            blog=blog_form.save(commit=False)
            blog.author=request.user
            photo.uploader=request.user
            photo.save()
            blog.photo=photo
            blog.save()
            return redirect('blog:home')
    context={
        'blog_form':blog_form,
        'photo_form':photo_form,
    }
    return render(request,'Blog/blog_add.html',context)

@login_required
def view_blog(request,blog_id):
    blog=get_object_or_404(Blog,id=blog_id)
    return render(request,'Blog/view_blog.html',{'blog':blog})

@login_required
def edit_blog(request,blog_id):
    blog=get_object_or_404(Blog,id=blog_id)
    edit_form=Forms.BlogForm(instance=blog)
    delete_form=Forms.DeleteBlogForm()
    context={
    'edit_form':edit_form,
    'delete_form':delete_form,
    }
    if request.method=="POST":
        if 'edit_blog' in request.POST:
            edit_form=Forms.BlogForm(request.POST,instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('blog:home')
        if 'delete_blog' in request.POST:
            delete_form=Forms.DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('blog:home')
    return render(request,'blog/edit_blog.html',context)