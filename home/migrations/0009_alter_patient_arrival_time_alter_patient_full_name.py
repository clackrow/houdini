# Generated by Django 4.1 on 2022-12-09 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_patient_full_name_alter_patient_arrival_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 9, 0, 33, 32, 365886, tzinfo=datetime.timezone.utc), verbose_name='Horário de chegada'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='full_name',
            field=models.CharField(default='<django.db.models.fields.charfield> <django.db.models.fields.charfield>', max_length=200, verbose_name='Nome completo'),
        ),
    ]
