"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contact/',views.contact.as_view(),name='contact'),
    path('about/',views.about,name='about'),
    path('singlepost/<id>/',views.singlepost,name='singlepost'),
    path('gellery/',views.gallery,name='gallery'),
    path('login/',views.Mylogin.as_view(),name='login'),
    path('logout/',views.Mylogout,name='logout'),
    path('signup/',views. singup.as_view(),name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addpost/',views.addpost,name='addpost'),
    path('update/<int:id>', views.updatepost, name='updatepost'),
    path('delete/<int:id>/', views.deletepost, name='deletepost'),
    path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('authername',views.authername,name='authername')
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 