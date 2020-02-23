# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    stuff="none"
    # E_mail = forms.EmailField(required=True)
    # subject = forms.CharField(required=True)
    # message = forms.CharField(widget=forms.Textarea, required=True)