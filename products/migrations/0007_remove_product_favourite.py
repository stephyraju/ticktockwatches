# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-23 06:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='favourite',
        ),
    ]