from django.shortcuts import render, HttpResponse, redirect
from django.apps import apps
from home.models import Patient
import datetime

# Create your views here.
def start_appointment(request, patient_uuid):
    if not request.user.is_authenticated: return redirect('/')
    model = Patient.objects.get(uuid=patient_uuid)
    context = {
        'name': str(model),
        'age': (datetime.date.today().year - model.birth.year),
        'uuid': model.uuid,
        'appointment_reason': model.appointment_reason,
    }
    if request.method == 'POST': 
        anamnese = request.POST.get('new_appointment')
        if anamnese is None or len(anamnese) < 10: return redirect(f'/appointment/{model.uuid}')
        save_appointment(anamnese, model, request.user)
        return redirect(f'/appointment/{model.uuid}')
    else:
        return render(request, 'appointment.html', context=context)


def save_appointment(anamnese, patient, professional):
    time_now = str(datetime.datetime.now().strftime("%d-%m-%y -> %H:%M"))
    if 'medico' in str(professional.groups.all()):
        med_record = patient.med_record
        med_record[f'{str(professional)} ({time_now})'] = anamnese
        patient.med_record = med_record
        patient.is_waiting_fordoctor = False
    if 'nutricionista' in str(professional.groups.all()):
        nutri_record = patient.nutri_record
        nutri_record[f'{str(professional)} ({time_now})'] = anamnese
        patient.nutri_record = nutri_record
        patient.is_waiting_fornutri = False
    
    try:
        patient.payment_record['not_payed'].append(f'Consulta com {str(professional)} na data {time_now}')
    except KeyError:
        patient.payment_record['not_payed'] = [f'Consulta com {str(professional)} na data {time_now}']
    patient.appointment_reason = ''
    patient.save()