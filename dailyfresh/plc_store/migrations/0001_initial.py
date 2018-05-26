# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stitle', models.CharField(max_length=20)),
                ('isPossess', models.BooleanField(default=False)),
                ('spai', models.IntegerField()),
                ('slie', models.IntegerField()),
                ('sceng', models.IntegerField()),
            ],
        ),
    ]
