from django.urls import path
from pictures import views

urlpatterns = [
    path('', views.index, name="index"),
    path('content/', views.content, name="content"),
]
