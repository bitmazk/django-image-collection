# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_collection', '0004_auto_20160113_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageslide',
            name='image_mobile',
            field=models.ImageField(blank=True, null=True, upload_to=b'image_slides', verbose_name='image_mobile'),
        ),
    ]
