# Generated by Django 4.1 on 2022-12-12 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_patient_full_name_alter_patient_arrival_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(default='', max_length=100, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='patient',
            name='payment_record',
            field=models.JSONField(blank=True, default={}, verbose_name='Histórico de pagamento'),
        ),
        migrations.AddField(
            model_name='patient',
            name='rg',
            field=models.CharField(default='', max_length=20, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 12, 16, 56, 6, 215741, tzinfo=datetime.timezone.utc), verbose_name='Horário de chegada'),
        ),
    ]
