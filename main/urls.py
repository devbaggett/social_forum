from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^accounts/', include('accounts_app.urls', namespace='accounts_app')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
