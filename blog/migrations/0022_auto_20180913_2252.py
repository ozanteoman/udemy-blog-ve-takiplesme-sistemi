# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-13 19:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0021_auto_20180912_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='isim',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='soyisim',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='icerik',
            field=models.TextField(max_length=1000, null=True, verbose_name='Yorum'),
        ),
    ]
