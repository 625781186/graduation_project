# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plc_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeinfo',
            name='sceng',
            field=models.IntegerField(verbose_name=b'\xe5\xb1\x82'),
        ),
        migrations.AlterField(
            model_name='storeinfo',
            name='slie',
            field=models.IntegerField(verbose_name=b'\xe5\x88\x97'),
        ),
        migrations.AlterField(
            model_name='storeinfo',
            name='spai',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92'),
        ),
        migrations.AlterField(
            model_name='storeinfo',
            name='stitle',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\xba\x93\xe4\xbd\x8d\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
