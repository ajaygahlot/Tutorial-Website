# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180211_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('faculty_no', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('cpi', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
    ]
