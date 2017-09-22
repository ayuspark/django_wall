# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 04:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0003_auto_20170921_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='posted_to_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages_posted_to', to='wall.MyUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='posted_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_posted_by', to='wall.MyUser'),
        ),
    ]