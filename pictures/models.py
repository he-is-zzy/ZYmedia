import datetime

from django.utils import timezone
from django.db import models


# Create your models here.


class style(models.Model):
    style_name = models.CharField(max_length=200)
    style_num = models.CharField(max_length=10)

    def __str__(self):
        return self.style_name


class info(models.Model):
    info_path = models.CharField(max_length=200)
    info_size = models.CharField(max_length=20)
    info_date = models.DateField('date published')

    def recently(self):
        return self.info_date >= timezone.now()-datetime.timedelta(days=1)

    def __str__(self):
        return self.info_path
