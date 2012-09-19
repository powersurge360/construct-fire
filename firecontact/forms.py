from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        send_mail(
            self.cleaned_data["subject"],
            self.cleaned_data["message"],
            self.cleaned_data["email"],
            [settings.CONTACT_EMAIL],
        )
