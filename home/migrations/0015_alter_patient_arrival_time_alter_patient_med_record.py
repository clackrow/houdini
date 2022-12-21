# Generated by Django 4.1.3 on 2022-12-21 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_patient_arrival_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='arrival_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, verbose_name='Horário de chegada'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='med_record',
            field=models.JSONField(blank=True, default=dict, verbose_name='Prontuário médico'),
        ),
    ]
