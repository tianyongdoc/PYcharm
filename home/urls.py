

from django.conf.urls import url,include

from . import  views


urlpatterns = [

    url(r'^home/', views.home,name='home'),
    url(r'^login/', views.login,name='login'),
    url(r'^register/', views.register,name='register'),
    url(r'^search/', views.search,name='search'),

    url(r'^zz/', views.zz,name='zz'),


]

