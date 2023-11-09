from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='blog'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/photo/',views.photo_upload,name='photo_upload'),
    path('home/blog_add/',views.blog_add,name='blog_add'),
    path('home/blog/<int:blog_id>',views.view_blog,name='view_blog'),
    path('home/<int:blog_id>/edit',views.edit_blog,name='edit_blog'),
    path('home/follow-users/',views.follow_users,name='follow_users'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)