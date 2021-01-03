from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import info


def index(request):
    return render(request, 'pictures/index.html')
