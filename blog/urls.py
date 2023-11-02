from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='blog'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/photo/',views.photo_upload,name='photo_upload'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)