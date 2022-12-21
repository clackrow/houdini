from django.shortcuts import render, HttpResponse, redirect
from home.models import Patient
import datetime

# Create your views here.
def display_patient(request, search_term):
    if not request.user.is_authenticated: return redirect('/')
    if 'secretaria' in str(request.user.groups.all()): return redirect(f'/sec/{search_term}')
    patient = Patient.objects.get(uuid=search_term)

    context = {
        'name': str(patient),
        'age': (datetime.date.today().year - patient.birth.year),
        'uuid': patient.uuid,
    }
    selection = request.GET.get('professional')
    if selection == 'nutri': context['med_rec'] = reversed([[item, patient.nutri_record[item]] for item in patient.nutri_record])
    if selection == 'doc': context['med_rec'] = reversed([[item, patient.med_record[item]] for item in patient.med_record])

    return render(request, 'display_patient.html', context=context)


def search_patient(request):
    if not request.user.is_authenticated: return redirect('/')
    search_term = f'{request.GET.get("termo_pesquisa")}'.lower()
    all_patients = Patient.objects.all()

    results = []
    for patient in all_patients:
        if search_term in str(patient).lower() or search_term in patient.cpf or search_term in str(patient.uuid): 
            results.append([str(patient), (datetime.date.today().year - patient.birth.year), patient.cpf, patient.uuid])

    context = {
        'resultados': results
    }
    return render(request, 'search_patient.html', context=context)