import os
import operator

from django.shortcuts import render
from django.http import HttpResponse
from .models import pictures, root, child
from pyscript import app_pic


# Create your views here.
def navigate(request):
    return render(request, 'pictures/Navigate.html')


def add_path(request):
    return render(request, 'pictures/add.html')


def cal_path(request):
    if request.method == 'POST':
        # 获取提交信息
        root_path = request.POST["root_path"]
        root_type = root_path.split('\\')[-1]

        print("root_path", root_path)
        print("root_type", root_path.split('\\')[-1])

        # 检测root是否重复
        root_list = root.objects.all()
        if root_list.count() == 0:
            print("空，开始添加新元素")
            root.objects.create(root_type=root_type, root_path=root_path)
        else:
            print("非空")
        for i in root_list:
            if i.root_path == root_path:
                print("该路径已存在")
            else:
                print("创建")
                root.objects.create(root_type=root_type, root_path=root_path)

        # 检测child更新
        childs = app_pic.find_child_dir(root_path)
        flag = 0

        for j in childs:
            print("开始寻找:", j)
            for i in child.objects.filter(father_path=root.objects.get(root_path=root_path)):
                if j == i.child_path:
                    print("已存在")
                    flag = 1
            if flag == 0:
                print("在当前目录未找到，开始创建新元素")
                child.objects.create(father_path=root.objects.get(root_path=root_path), child_path=j,
                                     dir_num=app_pic.dir_count(j))

        # 检测pictures更新
        flag = 0
        child_list = child.objects.filter(father_path=root.objects.get(root_path=root_path))
        for i in child_list:
            print("开始寻找", i.child_path)
            pic_set = app_pic.find_pictures(i.child_path)
            pics = pictures.objects.filter(father_path=child.objects.get(child_path=i.child_path))
            for j in pic_set:
                for k in pics:
                    if j.pic_path == k.pic_path:
                        print("已存在")
                        flag = 1
                        break
                if flag == 0:
                    print("当前目录未找到")
                    print("创建", j.pic_title)
                    pictures.objects.create(father_path=child.objects.get(child_path=i.child_path),
                                            pic_title=j.pic_title,
                                            pic_path=j.pic_path,
                                            pic_cover=j.pic_cover,
                                            pic_num=j.pic_num)

    return render(request, 'pictures/add_success.html')


def index(request):
    pic_log = []
    pic_list = pictures.objects.all()
    for i in pic_list:
        element = i
        element.pic_cover = i.pic_cover.replace('\\', '/').replace('D:/H', 'http://192.168.31.42:8080/files')
        pic_log.append(element)

    dic_set = {
        'dic': pic_log,
    }
    return render(request, 'pictures/index.html', dic_set)


def content(request):
    file_list = []
    if request.method == 'POST':
        dir_path = request.POST['path']
        print(request.POST['path'])
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_list.append(os.path.join(root, file).replace('\\', '/').replace('D:/H', 'http://192.168.31.42:8080/files'))
    path = {
        'path': file_list
    }
    return render(request, 'pictures/content.html', path)
