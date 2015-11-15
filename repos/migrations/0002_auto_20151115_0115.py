# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeploymentScripts',
            new_name='DeploymentScript',
        ),
        migrations.RenameModel(
            old_name='Repos',
            new_name='Repo',
        ),
        migrations.RenameModel(
            old_name='Servers',
            new_name='Server',
        ),
    ]
