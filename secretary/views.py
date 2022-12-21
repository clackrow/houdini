from django.shortcuts import render, redirect, HttpResponse
from home.models import Patient
import datetime
import uuid

# Create your views here.
def welcomepage(request):
    if not request.user.is_authenticated: return redirect('/')
    filter = request.GET.get('professional')
    waiting_room = create_waitingroom_list(filter)
    context = {
        'workplace': 'Spa clínica',
        'professional': request.user,
        'patients': waiting_room,
    }
    return render(request, 'sec_homepage.html', context=context)

def new_patient(request):
    if not request.user.is_authenticated: return redirect('/')
    if request.method == 'GET': return render(request, 'new_patient.html')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    gender = request.POST.get('gender')
    rg = request.POST.get('rg')
    cpf = request.POST.get('cpf')
    birth = request.POST.get('birth')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    email = request.POST.get('mail')
    uuid_=str(uuid.uuid4())
    Patient.objects.create(
        uuid=uuid_,
        first_name=first_name,
        last_name=last_name,
        rg=rg,
        cpf=cpf,
        birth=birth,
        address=address,
        phone=phone,
        email=email,
        )
    return redirect('/sec/new_patient/')
    
def payment_screen(request, uuid):
    if not request.user.is_authenticated: return redirect('/')
    patient = Patient.objects.get(uuid=uuid)
    try:
        not_payed = patient.payment_record['not_payed']
    except:
        not_payed = []
    try:
        payed = patient.payment_record['payed']
    except:
        payed = []
    context = {
        'name': str(patient),
        'uuid': patient.uuid,
        'payed': payed,
        'not_payed': not_payed
    }
    if request.method == 'GET': return render(request, 'payment_screen.html', context=context)
    for item in request.POST:
        price = request.POST.get(f'{item}')
        if len(price) == 0: continue
        if item == 'csrfmiddlewaretoken': continue

        patient.payment_record['not_payed'].pop(patient.payment_record['not_payed'].index(item))
        try:
            patient.payment_record['payed'].append(f'R${price} - {item} ({str(datetime.datetime.now().isoformat("|", "minutes"))})')
        except KeyError:
            patient.payment_record['payed'] = [f'R${price} - {item} ({str(datetime.datetime.now().isoformat("|", "minutes"))})']
        patient.save()
    return redirect(f'/sec/payments/{patient.uuid}')
    

def create_waitingroom_list(filter):
    every_patient = Patient.objects.all()
    waiting_room = []
    if filter == 'medico': waiting_room = [patient for patient in every_patient if patient.is_waiting_fordoctor]
    if filter == 'nutricionista': waiting_room = [patient for patient in every_patient if patient.is_waiting_fornutri]
    formated_list = [[str(patient), (datetime.date.today().year - patient.birth.year), patient.uuid, patient.arrival_time, patient.appointment_reason] for patient in waiting_room]
    return formated_list



def patient_screen(request, uuid):
    if not request.user.is_authenticated: return redirect('/')
    patient = Patient.objects.get(uuid=uuid)
    if request.method == 'GET':
        context = {
            'name': f'{patient.first_name} {patient.last_name}',
            'uuid': uuid,
            'cpf': patient.cpf,
            'rg': patient.rg,
            'birth': patient.birth,
            'add': patient.address,
            'phone': patient.phone,
            'waiting_doc': patient.is_waiting_fordoctor,
            'waiting_nutri': patient.is_waiting_fornutri,
            'doc_time': patient.arrival_time,
        }
        return render(request, 'patient_screen.html', context=context)
    
    if request.method == 'POST':
        html_bool = {'on': True, None: False}
        is_waiting_doc = html_bool[request.POST.get('waiting_doc')]
        is_waiting_nutri = html_bool[request.POST.get('waiting_nutri')]
        arrival_time = request.POST.get('arrival_time')
        patient.is_waiting_fordoctor = is_waiting_doc
        patient.is_waiting_fornutri = is_waiting_nutri
        patient.arrival_time = arrival_time
        patient.save()
        return redirect(f'/sec/{uuid}')