# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-05-29 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payutoken',
            name='TOKEN_HASH',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'Token Hash'),
        ),
    ]
