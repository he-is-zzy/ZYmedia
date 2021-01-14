from django.db import models


# Create your models here.

class root(models.Model):
    root_type = models.CharField(max_length=50, null=True, blank=True)
    root_path = models.CharField(max_length=200, null=True, blank=True, unique=True)


class child(models.Model):
    father_path = models.ForeignKey('root', on_delete=models.CASCADE)
    child_path = models.CharField(max_length=200, null=True, blank=True)
    dir_num = models.CharField(max_length=20, null=True, blank=True)


class pictures(models.Model):
    father_path = models.ForeignKey("child", on_delete=models.CASCADE)
    pic_title = models.CharField(max_length=100, null=True, blank=True)
    pic_path = models.CharField(max_length=200, null=True, blank=True)
    pic_num = models.CharField(max_length=10, null=True, blank=True)
    pic_author = models.CharField(max_length=50, null=True, blank=True)
    pic_cover = models.CharField(max_length=100, null=True, blank=True)
    pic_tag = models.CharField(max_length=20, null=True, blank=True)
