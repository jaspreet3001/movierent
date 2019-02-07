from django.urls import path,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from movie_rental.models import movie
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index,name='home'),
    path('logout/', views.userlogout, name='logout'),
    path('login/', views.userlogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('movies/', views.movieslist.as_view(),name='movies'),
    path('available/', views.available,name='available'),
    path('customers/', views.customers,name='customers'),
    path('rented/', views.rented,name='rented'),
    path('assign/', views.assign,name='assign'),
    path('newcustomer/', views.add_customer,name='newcustomer'),
    path('newmovie/', views.add_movie,name='newmovie'),
    path('movies/remove/<int:m_num>/',views.delete_movie,name='delete_movie'),
    path('customers/remove/<int:c_num>',views.delete_customer,name='delete_customer')
] 