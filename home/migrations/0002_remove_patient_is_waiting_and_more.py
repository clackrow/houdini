# Generated by Django 4.1 on 2022-12-08 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='is_waiting',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='medical_record',
        ),
        migrations.AddField(
            model_name='patient',
            name='appointment_reason',
            field=models.CharField(blank=True, default='Retorno', max_length=200, verbose_name='Motivo da consulta'),
        ),
        migrations.AddField(
            model_name='patient',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 8, 18, 28, 45, 420827, tzinfo=datetime.timezone.utc), verbose_name='Horário de chegada'),
        ),
        migrations.AddField(
            model_name='patient',
            name='cpf',
            field=models.IntegerField(default=0, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='patient',
            name='is_waiting_fordoctor',
            field=models.BooleanField(default=False, verbose_name='Esperando consulta médica'),
        ),
        migrations.AddField(
            model_name='patient',
            name='is_waiting_fornutri',
            field=models.BooleanField(default=False, verbose_name='Esperando consulta nutricional'),
        ),
        migrations.AddField(
            model_name='patient',
            name='med_record',
            field=models.JSONField(default={}, verbose_name='Prontuário médico'),
        ),
        migrations.AddField(
            model_name='patient',
            name='nutri_record',
            field=models.JSONField(default={}, verbose_name='Prontuário nutricional'),
        ),
    ]
