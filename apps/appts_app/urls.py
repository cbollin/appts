from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^appts$', views.appts, name='appts'),
    url(r'^add$', views.add, name='add'),
    url(r'^edit/(?P<appt_id>\d+)$', views.edit, name='edit'),
    url(r'^update/(?P<appt_id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<appt_id>\d+)$', views.delete, name='delete'),
    url(r'^logout$', views.logout, name='logout'),
]
