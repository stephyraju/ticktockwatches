# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-06 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_topbrands'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='topbrands',
            new_name='topbrand',
        ),
    ]