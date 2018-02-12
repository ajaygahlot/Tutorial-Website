from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main/',include('main.urls')),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
