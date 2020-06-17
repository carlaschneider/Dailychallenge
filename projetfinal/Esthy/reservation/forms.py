from django import forms
from .models import Calendar
from django.forms import ModelForm


class calendar(ModelForm):
    date_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

    class Meta:
        model = Calendar
        fields = ['nom', 'prenom', 'email', 'date_time']