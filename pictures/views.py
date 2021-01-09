import os

from django.shortcuts import render
from django.http import HttpResponse
from .models import pictures
from pyscript import app_pic


# Create your views here.
def navigate(request):
    return render(request, 'pictures/Navigate.html')


def index(request):
    pic_data = pictures.objects.all()
    pic_dic = {
        'dic': pic_data,
    }
    for i in pic_data:
        print(i.pic_title)
    # # 图像路径
    # base_path = R"D:\H\Manga\[MG] Doujinshi\[雑誌] 快楽天 WEEKLY"
    # path = base_path.replace("\\", "/")
    # # 获取内容
    # pic_log, dir_count = app_pic.find_pictures(path)
    # # 更新/创建
    # for i in range(dir_count):
    #     pictures.objects.update(pic_title=pic_log[i].pic_title,
    #                             pic_cover=pic_log[i].pic_cover,
    #                             pic_path=pic_log[i].pic_path,
    #                             pic_num=pic_log[i].pic_num)
    # pic_dic = {
    #     'dic': pic_log,
    # }
    return render(request, 'pictures/index.html', pic_dic)


def content(request):
    dir_path = ''
    file_list = []
    if request.method == 'POST':
        dir_path = request.POST['path']
        print(request.POST['path'])
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_list.append(os.path.join(root, file).replace('D:/H', 'http://192.168.1.107:8080/files'))
    path = {
        'path': file_list
    }
    return render(request, 'pictures/content.html', path)
