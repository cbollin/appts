# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='Preeya', max_length=45),
            preserve_default=False,
        ),
    ]
