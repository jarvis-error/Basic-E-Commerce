from django.urls import path
from . import views

urlpatterns = [
    path('',views.first,name='first'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('user',views.user,name='user'),
    path('products',views.products,name='products'),
]
