# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MicroService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('repo_url', models.URLField(null=True)),
                ('documentation_url', models.URLField(null=True)),
                ('staging_url', models.URLField(null=True)),
                ('live_url', models.URLField(null=True)),
                ('api_explorer_url', models.URLField(null=True)),
                ('maturity', models.PositiveIntegerField()),
                ('owner', models.PositiveIntegerField(help_text=b'User ID of the person responsible for this service')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
