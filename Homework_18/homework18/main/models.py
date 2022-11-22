from django.db import models


class Model1(models.Model):
    part_id = models.IntegerField()
    part = models.CharField(max_length=100)
    cat = models.IntegerField()


class Model2(models.Model):
    cat_numb = models.IntegerField()
    cat_name = models.CharField(max_length=100)
    price = models.FloatField()

