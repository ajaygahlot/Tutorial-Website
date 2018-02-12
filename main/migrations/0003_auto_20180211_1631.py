# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_binarytee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BinaryTee',
            new_name='BinaryTree',
        ),
    ]
