from django.db import models


# Create your models here.

class pic_type(models.Model):
    pic_type = models.CharField(max_length=50)
    pic_path = models.CharField(max_length=200)


class pictures(models.Model):
    belong_type = models.ForeignKey("pic_type",on_delete=models.CASCADE)
    pic_title = models.CharField(max_length=100)
    pic_path = models.CharField(max_length=200)
    pic_num = models.CharField(max_length=10)
    pic_author = models.CharField(max_length=50)
    pic_cover = models.CharField(max_length=100)
    pic_tag = models.CharField(max_length=20)
