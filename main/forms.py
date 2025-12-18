from django import forms
from .models import Appointment
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, required=False)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time', 'message']

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get('start')
        end = cleaned.get('end')
        if start and end and start >= end:
            raise ValidationError("End must be after start.")
        if start and end:
            from .models import Appointment
            overlapping = Appointment.objects.filter(start__lt=end, end__gt=start)
            if overlapping.exists():
                raise ValidationError("This time conflicts with an existing appointment.")
        return cleaned
 