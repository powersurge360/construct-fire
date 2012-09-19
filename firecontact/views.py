from django.core.urlresolvers import reverse
from django.views.generic import FormView

from firecontact.forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "firecontact/contact.html"

    def get_success_url(self):
        return reverse("firecontact:contact")

    def form_valid(self, form):
        form.send_email()
        return super(ContactFormView, self).form_valid(form)
