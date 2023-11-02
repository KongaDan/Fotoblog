from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView

app_name='authentication'
urlpatterns = [
    
    path('',LoginView.as_view(template_name='authentication/login.html',redirect_authenticated_user=True),name='login'),
    path('signup/',views.signup_page,name='signup'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('password/change/',PasswordChangeView.as_view(template_name='authentication/password_change.html'),name='password_change'),
    path('password/changeDone/',PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'),name='password_change_done'),
    path('Profil/photo/',views.upload_profile_photo,name='profil_photo'),
]
