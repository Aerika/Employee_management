from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^department/$', views.department_list, name = 'department-list'),
    url (r'^employee/?$', views.employee_list, name='employee-list'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^create/$', views.create, name='create'),
    url(r'^add/$', views.add, name='create'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
    url (r'^d-edit/(?P<pk>\d+)/$', views.d_edit, name='edit'),

    url (r'^d-delete/(?P<pk>\d+)/$', views.d_delete, name='delete'),
#url(r'^edit/$', views.edit, name='edit'),


]

