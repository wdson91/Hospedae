# Generated by Django 4.1 on 2022-09-12 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_codigo', models.BigIntegerField()),
                ('promo_chave', models.CharField(max_length=255)),
                ('promo_tipo', models.CharField(max_length=255)),
                ('promo_valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('promo_dhinicio', models.DateTimeField(default=datetime.datetime(2022, 9, 12, 19, 34, 5, 852839))),
                ('promo_dhfim', models.DateTimeField(default=datetime.datetime(2022, 9, 12, 19, 34, 5, 852839))),
                ('promo_situacao', models.CharField(max_length=255)),
            ],
        ),
    ]
