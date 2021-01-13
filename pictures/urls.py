from django.urls import path
from pictures import views

urlpatterns = [
    path('', views.navigate, name="navigate"),
    path('content/', views.content, name="content"),
    path('add/', views.add_path, name="add"),
    path('success/', views.cal_path, name="cal"),
]
