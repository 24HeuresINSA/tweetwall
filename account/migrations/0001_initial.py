# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-01 09:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=250, verbose_name='nom')),
                ('name', models.CharField(max_length=250, verbose_name='identifiant')),
                ('application_id', models.CharField(max_length=250, verbose_name='application id')),
                ('application_secret', models.CharField(max_length=250, verbose_name='application secret')),
                ('token_endpoint', models.CharField(max_length=1000, verbose_name='url pour jetons')),
                ('authorization_endpoint', models.CharField(max_length=1000, verbose_name='url pour autorisation')),
                ('enabled', models.BooleanField(verbose_name='actif')),
            ],
            options={
                'verbose_name': 'Service OAuth',
            },
        ),
        migrations.CreateModel(
            name='OAuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=250)),
                ('auth_token_expiration', models.DateTimeField()),
                ('renew_token', models.CharField(blank=True, max_length=250, null=True)),
                ('renew_token_expiration', models.DateTimeField(blank=True, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='account.OAuthService', verbose_name='service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'Jeton OAuth',
            },
        ),
    ]
