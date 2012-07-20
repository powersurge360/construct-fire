from django.conf.urls import patterns, url
from fireblog.views import EntryListView

urlpatterns = patterns('',
    url(r'^entries$', EntryListView.as_view(), name="home"),
)

namespace = urlpatterns, "fireblog", ""
