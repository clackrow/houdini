from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Patient
import datetime

# Create your views here.
def welcomepage(request):
    if not request.user.is_authenticated: return redirect('/')
    waiting_room = create_waitingroom_list(request.user)
    context = {
        'workplace': 'Clínica Sou Saudável👍',
        'professional': request.user,
        'patients': waiting_room,
        'secretary': False,
    }
    if str(request.user.groups.all()[0]) == 'secretaria': return redirect('/sec/?professional=medico#')
    return render(request, 'welcomepage.html', context=context)


def logoutcommand(request):
    logout(request)
    print('deslogando', request.user)
    return redirect('/')

def create_waitingroom_list(user):
    every_patient = Patient.objects.all()
    waiting_room = []
    if str(user.groups.all()[0]) == 'medico': waiting_room = [patient for patient in every_patient if patient.is_waiting_fordoctor]
    if str(user.groups.all()[0]) == 'nutricionista': waiting_room = [patient for patient in every_patient if patient.is_waiting_fornutri]
    formated_list = [[str(patient), (datetime.date.today().year - patient.birth.year), patient.uuid, patient.arrival_time, patient.appointment_reason] for patient in waiting_room]
    return formated_list


