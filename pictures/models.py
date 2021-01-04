from django.db import models


# Create your models here.


class pictures(models.Model):
    pic_title = models.CharField(max_length=100)
    pic_path = models.CharField(max_length=200)
    pic_num = models.CharField(max_length=10)
    pic_author = models.CharField(max_length=50)
    pic_cover = models.CharField(max_length=100)
    pic_tag1 = models.CharField(max_length=20)
    pic_tag2 = models.CharField(max_length=20)
    pic_tag3 = models.CharField(max_length=20)
    pic_tag4 = models.CharField(max_length=20)
    pic_tag5 = models.CharField(max_length=20)
    pic_tag6 = models.CharField(max_length=20)
    pic_tag7 = models.CharField(max_length=20)
