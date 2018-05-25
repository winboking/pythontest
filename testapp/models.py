# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Sale_order(models.Model):

    name = models.CharField(max_length=64, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    sale_type_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sale_order'

class SaleOrderLine(models.Model):

    order_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_line'

class Sale_Type(models.Model):

    t_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_type'
