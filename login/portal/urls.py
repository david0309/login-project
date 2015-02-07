from django.conf.urls import patterns, url
from portal.views import portal_main_page

urlpatterns = patterns('',

    # Main web portal entrance.
    url(r'^$', portal_main_page),

)