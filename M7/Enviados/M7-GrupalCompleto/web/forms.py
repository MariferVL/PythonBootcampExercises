from django import forms
from . models import *

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ('name', 'subject', 'message', 'sender', 'cc_myself',)
