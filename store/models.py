import os
import datetime
from django.db import models


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_hidden = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    meta_title = models.CharField(max_length=150)
    meta_keywords = models.CharField(max_length=150)
    meta_description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path)
    small_description = models.CharField(max_length=150)
    quantity = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True, null=True)
    original_price = models.FloatField()
    selling_price = models.FloatField()
    is_hidden = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    tag = models.CharField(max_length=150)
    meta_title = models.CharField(max_length=150)
    meta_keywords = models.CharField(max_length=150)
    meta_description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
