# Generated by Django 2.1.5 on 2019-01-25 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_collection', '0010_auto_20160330_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageslide',
            name='image',
            field=models.ImageField(upload_to='image_slides', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='imageslide',
            name='image_mobile',
            field=models.ImageField(blank=True, null=True, upload_to='image_slides', verbose_name='image_mobile'),
        ),
    ]
