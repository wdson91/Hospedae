# Generated by Django 4.1 on 2022-09-12 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seg', '0004_alter_log_log_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='log_data',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 19, 34, 5, 303729)),
        ),
    ]
