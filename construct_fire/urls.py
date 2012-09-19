from django.conf.urls import patterns, include, url
from django.contrib import admin

import fireblog.urls
import firecontact.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(*fireblog.urls.namespace)),
    url(r'^contact/', include(*firecontact.urls.namespace)),
)
