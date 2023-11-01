from django.urls import path
from . import views
app_name='authentication'

urlpatterns = [
    
    path('',views.LoginPageView.as_view(),name='login'),
    path('logout/',views.logout_page,name='logout'),
]
