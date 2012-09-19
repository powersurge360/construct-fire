from django.conf.urls import patterns, url

from firecontact.views import ContactFormView

urlpatterns = patterns('',
    url(r'^$', ContactFormView.as_view(), name="contact"),
)

namespace = urlpatterns, "firecontact"
