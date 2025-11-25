from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Project, Skill, Education, Appointment
from .forms import AppointmentForm, ContactForm
from datetime import date

def home(request):
    recent = Project.objects.order_by('-created_at')[:3]
    return render(request, 'home.html', {'recent_projects': recent})

def about(request):
    return render(request, 'about.html')

def projects(request):
    qs = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': qs})

def skills_education(request):
    skills = Skill.objects.all()
    education = Education.objects.all()
    return render(request, 'skills_education.html', {'skills': skills, 'education': education})

def contact(request):
    contact_form = ContactForm(prefix="contact")
    appointment_form = AppointmentForm()  
    message_sent = False
    appointment_created = False

    if request.method == "POST":
        if "send_contact" in request.POST:
            contact_form = ContactForm(request.POST, prefix="contact")
            if contact_form.is_valid():
                message_sent = True

        elif "schedule_appointment" in request.POST:
            appointment_form = AppointmentForm(request.POST)  
            if appointment_form.is_valid():
                appointment_form.save()
                appointment_created = True
                return redirect('/contact?success=1') 

    appointments = Appointment.objects.order_by("date", "time")

    return render(request, "contact.html", {
        "contact_form": contact_form,
        "appointment_form": appointment_form,
        "appointments": appointments,
        "message_sent": message_sent,
        "appointment_created": appointment_created,
    })

def appointment_events(request):
    appointments = Appointment.objects.filter(date__gte=date.today())

    events = []
    for a in appointments:
        time_str = a.time.strftime("%H:%M") if a.time else "10:00"
        start_datetime = f"{a.date}T{time_str}"

        events.append({
            "title": a.name,
            "start": start_datetime,
            "allDay": False,
        })

    return JsonResponse(events, safe=False)

def appointment_success(request):
    return render(request, "appointment_success.html")

def contact_thanks(request):
    return render(request, "contact_thanks.html")

def scheduler(request):
    return render(request, "scheduler.html")
