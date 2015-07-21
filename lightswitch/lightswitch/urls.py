from django.conf.urls import patterns, include, url
from django.core.context_processors import csrf
from django.contrib import admin
from main.views import HomeView, ControlledView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lightswitch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^controlled/$', ControlledView.as_view(), name='controlled'),
    url(r'^admin/', include(admin.site.urls)),
)
