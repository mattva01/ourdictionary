from django.conf.urls.defaults import patterns, include, url
from django.views.generic import CreateView, ListView, DetailView, RedirectView
from wordviewer.models import WordEntry
from wordviewer.views import register, WordEntryCreationView, WordEntryUpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout, password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm
# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url="/words/")),
    url(r'^create_entry/$', WordEntryCreationView.as_view(template_name="wordviewer/wordentry_form.html")),
    url(r'^update_entry/(?P<pk>\d+)/$', WordEntryUpdateView.as_view(template_name="wordviewer/wordentry_update.html")),
    url(r'^words/$', ListView.as_view(model=WordEntry,queryset=WordEntry.objects.order_by('name'))),
    url(r'^words/(?P<pk>\d+)/$', DetailView.as_view(model=WordEntry)), 
    url(r'^register/$',register),
    url(r'^password_change/$',password_change),
    url(r'^password_change/done/$',password_change_done),
    url(r'^password_reset/$',password_reset),
    url(r'^password_reset/done/$',password_reset_done),
    url(r'^password_reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm),
    url(r'^login/$',login),
    url(r'^logout/$',logout,{'next_page': '/'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
