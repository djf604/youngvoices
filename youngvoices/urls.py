from django.conf.urls import url
from django.views.generic import TemplateView

from youngvoices import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='youngvoices/index.html')),
    url(r'^about-us/$', TemplateView.as_view(template_name='youngvoices/about_mia.html')),
    url(r'^safe-spaces/$', TemplateView.as_view(template_name='youngvoices/services_sofia.html')),
    url(r'^message-box/$', TemplateView.as_view(template_name='youngvoices/message1.html')),
    url(r'^our-stories/$', TemplateView.as_view(template_name='youngvoices/blog2.html')),
    url(r'^register/$', views.register),
    url(r'^logout/$', views.logout_),
    url(r'^quiz/$', views.quiz)
]