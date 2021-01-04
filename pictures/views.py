import os

from django.shortcuts import render
from django.http import HttpResponse
from .models import pictures
from pyscript import app_pic


# Create your views here.

def index(request):
    # 图像路径
    path = R"D:\H\Pictures and Photobooks\[PAP] Cosplay\SayaTheFox"
    # 获取内容
    pic_log, dir_count = app_pic.find_pictures(path)
    # 更新/创建
    for i in range(dir_count):
        pictures.objects.update(pic_title=pic_log[i].pic_title,
                                pic_cover=pic_log[i].pic_cover,
                                pic_path=pic_log[i].pic_path,
                                pic_num=pic_log[i].pic_num)
    pic_dic = {
        'dic': pic_log,
    }
    return render(request, 'pictures/index.html', pic_dic)
