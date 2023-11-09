from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from . models import Photo,Blog
from . import Forms

@login_required
def home(request):
    photos=Photo.objects.all()
    blogs=Blog.objects.all()
    return render(request,'blog/home.html',{'photos':photos,'blogs':blogs})

@login_required
@permission_required('blog.add_photo',raise_exception=True)
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
@permission_required(perm='blog.add_blog')
def blog_add(request):
    blog_form=Forms.BlogForm()
    photo_form=Forms.PhotoForm()
    if request.method=="POST":
        blog_form=Forms.BlogForm(request.POST)
        photo_form=Forms.PhotoForm(request.POST,request.FILES)
        if all([blog_form.is_valid(),photo_form.is_valid()]):
            photo=photo_form.save(commit=False)
            photo.uploader=request.user
            photo.save()
            blog=blog_form.save(commit=False)
            blog.photo=photo
            blog.save()
            blog.contributors.add(request.user,through_defaults={'contribution':'Auteur principal'})
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
@permission_required(perm='blog.change_blog')
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

@login_required
def follow_users(request):
    form=Forms.FolowUserForm(instance=request.user)
    if request.method =='POST':
        form=Forms.FolowUserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    return render(request,'blog/follow_users_form.html',{'form':form})