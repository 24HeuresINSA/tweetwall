# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-27 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='author_picture',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='validated_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='video',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]