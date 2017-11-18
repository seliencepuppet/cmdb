# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-28 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_auto_20170827_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='host_ip',
            new_name='ip_addr',
        ),
        migrations.RemoveField(
            model_name='host',
            name='host_group',
        ),
        migrations.AddField(
            model_name='host',
            name='host_groups',
            field=models.ManyToManyField(to='monitor.HostGroup', verbose_name='主机组'),
        ),
        migrations.AlterField(
            model_name='host',
            name='templates',
            field=models.ManyToManyField(to='monitor.Template', verbose_name='默认模板'),
        ),
    ]