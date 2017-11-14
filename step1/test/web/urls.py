from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^add_site/$', views.addSite, name='add_site'),
    url(r'^sites/$', views.sites, name='sites'),
]