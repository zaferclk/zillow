# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0004_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='states', to='listing_app.State'),
            preserve_default=False,
        ),
    ]