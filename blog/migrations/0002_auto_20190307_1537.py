# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-07 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='阅读量'),
        ),
    ]
