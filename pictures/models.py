from django.db import models


# Create your models here.

class root(models.Model):
    root_type = models.CharField(max_length=50)
    root_path = models.CharField(max_length=200)


class child(models.Model):
    father_path = models.ForeignKey('root', on_delete=models.CASCADE)
    chile_path = models.CharField(max_length=200)
    dir_num = models.CharField(max_length=20)


class pictures(models.Model):
    father_path = models.ForeignKey("child", on_delete=models.CASCADE)
    pic_title = models.CharField(max_length=100)
    pic_path = models.CharField(max_length=200)
    pic_num = models.CharField(max_length=10)
    pic_author = models.CharField(max_length=50)
    pic_cover = models.CharField(max_length=100)
    pic_tag = models.CharField(max_length=20)
