# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0003_auto_20160512_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='comments',
            field=models.CharField(blank=True, max_length=9000),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='description',
            field=models.CharField(blank=True, max_length=9000),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='product_description',
            field=models.CharField(blank=True, max_length=9000),
        ),
    ]
