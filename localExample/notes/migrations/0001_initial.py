# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-05 01:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=500, verbose_name='autor')),
                ('title', models.CharField(max_length=500, unique=True, verbose_name='Titulo')),
                ('note', models.TextField(verbose_name='Note')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario De la nota')),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'Notes',
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
    ]
