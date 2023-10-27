from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import login,logout,authenticate

def login_page(request):
    message=''
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                message=f'Vous etes connectes {user.username}'
                return redirect('blog:home')
            message='Invalid input'
    return render(request,'authentication\login.html',{'form':form,'message':message})
def logout_page(request):
    logout(request)
    return redirect('authentication:login')
