# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-27 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('image', models.URLField(max_length=300)),
                ('video', models.URLField(max_length=300)),
                ('video_is_gif', models.BooleanField(default=False)),
                ('author_name', models.CharField(max_length=50)),
                ('author_username', models.CharField(max_length=50)),
                ('author_picture', models.URLField(max_length=300)),
                ('published_at', models.DateTimeField()),
                ('provider_post_id', models.CharField(max_length=20)),
                ('validated_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('PE', 'En attente'), ('PU', 'Publié'), ('PR', 'Promu'), ('RE', 'Rejeté')], default='PE', max_length=2)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='social.Feed')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('TWI', 'Twitter'), ('INS', 'Instagram')], max_length=3)),
                ('app_id', models.CharField(max_length=100)),
                ('app_secret', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='social.Provider'),
        ),
        migrations.AddField(
            model_name='feed',
            name='providers',
            field=models.ManyToManyField(related_name='feeds', to='social.Provider'),
        ),
    ]
