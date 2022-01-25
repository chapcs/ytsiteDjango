from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('pricing.html', views.pricing, name="pricing"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('static/affiliate/assets/favi.ico'))),
]