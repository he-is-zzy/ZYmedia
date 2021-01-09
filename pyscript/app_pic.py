# -*- coding: utf-8 -*-
import os


# 类型根目录
def find_child_dir(root_path):
    dir_path = []
    for root, dirs, files in os.walk(root_path):
        for dir_name in dirs:
            father_path = os.path.abspath(os.path.dirname(os.path.join(root, dir_name)) + os.path.sep + ".")
            if father_path == root_path:
                dir_path.append(os.path.join(root, dir_name))
    return dir_path


# 寻找图片目录
def find_pictures(path):
    # 图片类
    class pic:
        pic_title = ''
        pic_path = ''
        pic_cover = ''
        pic_num = ''

        def __int__(self):
            self.pic_title = pic_title
            self.pic_path = pic_path
            self.pic_cover = pic_cover
            self.pic_num = pic_num

    pic_title = []  # 标题列表
    pic_path = []  # 路径列表
    pic_cover = []  # 封面列表
    pic_num = []  # 数量列表
    dir_count = 0  # 有效文件夹数
    pic_log = []  # 类列表

    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            # print(dir_name)
            dir_count = dir_count + 1
            pic_title.append(dir_name)
            pic_cover.append(find_cover(os.path.join(root, dir_name)))
            pic_path.append(os.path.join(root, dir_name))
            pic_num.append(file_count(os.path.join(root, dir_name)))

    for i in range(dir_count):
        tp = pic()
        tp.pic_title = pic_title[i]
        tp.pic_cover = pic_cover[i].replace('D:/H', 'http://192.168.1.107:8080/files')
        tp.pic_path = pic_path[i]
        tp.pic_num = pic_num[i]
        pic_log.append(tp)

    return pic_log, dir_count


# 寻找封面
def find_cover(dir_path):
    cover = ""
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            if file_name[:-4] == "cover" or file_name[:-4] == "Cover":
                print("cover:", file_name)
                cover = os.path.join(root, file_name)
                return cover
            else:
                continue
        cover = os.path.join(root, min(files))
    return cover


# 统计数量
def file_count(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for file_name in files:
            count = count + 1
    return count
