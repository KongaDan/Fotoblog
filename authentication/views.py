from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View

class LoginPageView(View):
    template_name='authentication/login.html'
    form_class=LoginForm
    def get(self,request):
        form=self.form_class()
        message=''
        return render(request,self.template_name,{'form':form,'message':message})
    def post(self,request):
        form=self.form_class(request.POST)
        message=''
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('blog:home')
            message='Invalid input'
        return render(request,self.template_name,{'form':form,'message':message})
def logout_page(request):
    logout(request)
    return redirect('authentication:login')
