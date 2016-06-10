# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-06 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='impressions_negated',
            new_name='impressions_negated_date1',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='impressions_positive',
            new_name='impressions_negated_date2',
        ),
        migrations.AddField(
            model_name='report',
            name='impressions_negated_date3',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='impressions_positive_date1',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='impressions_positive_date2',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='impressions_positive_date3',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
