# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-18 08:27
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190307_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='link_url',
            field=models.URLField(max_length=100, null=True, verbose_name='图片链接'),
        ),
    ]