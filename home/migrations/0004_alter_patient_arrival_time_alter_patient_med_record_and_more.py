# Generated by Django 4.1 on 2022-12-08 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_patient_arrival_time_alter_patient_med_record_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 8, 22, 39, 59, 415377, tzinfo=datetime.timezone.utc), verbose_name='Horário de chegada'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='med_record',
            field=models.JSONField(blank=True, default={}, editable=False, verbose_name='Prontuário médico'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nutri_record',
            field=models.JSONField(blank=True, default={}, editable=False, verbose_name='Prontuário nutricional'),
        ),
    ]
