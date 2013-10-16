from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social_circles.views.home', name='home'),
    # url(r'^social_circles/', include('social_circles.foo.urls')),

    # Maps '/admin/doc' to admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Maps '/admin/' to admin panel
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('friends.urls')),
)
