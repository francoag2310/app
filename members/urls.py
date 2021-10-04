from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', MemberLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
]
