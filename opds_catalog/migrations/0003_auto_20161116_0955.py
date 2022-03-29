# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opds_catalog', '0002_auto_20161115_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='docdate',
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='book',
            name='filename',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='book',
            name='filesize',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='format',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='book',
            name='path',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='book',
            name='registerdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='search_title',
            field=models.CharField(db_index=True, default=None, max_length=512),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(db_index=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='bookshelf',
            name='readtime',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='cat_name',
            field=models.CharField(db_index=True, max_length=190),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='path',
            field=models.CharField(db_index=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='series',
            name='search_ser',
            field=models.CharField(db_index=True, default=None, max_length=150),
        ),
    ]
