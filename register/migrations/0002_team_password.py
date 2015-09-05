# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='password',
            field=models.CharField(default=datetime.date(2015, 9, 1), max_length=100),
            preserve_default=False,
        ),
    ]
