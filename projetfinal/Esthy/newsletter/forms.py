from django import forms
from .models import NewsletterUser
from django.forms import ModelForm


class NewsletterForm(ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['firstname', 'lastname', 'email']