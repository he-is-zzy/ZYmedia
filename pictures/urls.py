from django.urls import path
from pictures import views

urlpatterns = [
    path('', views.navigate, name="navigate"),
    path('content/', views.content, name="content"),
]
