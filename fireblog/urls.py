from django.conf.urls import patterns, url
from fireblog.views import EntryListView, EntryDetailView

urlpatterns = patterns('',
    url(r'^$', EntryListView.as_view(), name="home"),
    url(r'^(?P<slug>[\w-]+)/$', EntryDetailView.as_view(), name="detail"),
)

namespace = urlpatterns, "fireblog", ""
