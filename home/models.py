from django.db import models
import uuid
import datetime
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField('Nome', max_length=30, blank=False)
    last_name = models.CharField('Sobrenome', max_length=30, blank=False)
    birth = models.DateField('Data de nascimento', default=datetime.date(1997, 10, 19), blank=False)
    cpf = models.CharField('CPF', default='', max_length=11)
    rg = models.CharField('RG', default='', max_length=20)
    phone = models.CharField('Telefone', default='', max_length=15)
    address = models.CharField('Endereço', default='', max_length=200)
    email = models.CharField('Email', default='', max_length=100)
    appointment_reason = models.CharField('Motivo da consulta', max_length=200, default='Retorno', blank=True)
    arrival_time = models.TimeField('Horário de chegada', default=timezone.now, blank=True)
    is_waiting_fordoctor = models.BooleanField('Esperando consulta médica', default=False)
    is_waiting_fornutri = models.BooleanField('Esperando consulta nutricional', default=False)
    med_record = models.JSONField('Prontuário médico', default=dict, blank=True)
    nutri_record = models.JSONField('Prontuário nutricional', default=dict, blank=True)
    payment_record = models.JSONField('Histórico de pagamento', default=dict, blank=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

