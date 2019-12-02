from django.urls import path
from . import views


urlpatterns = [

   path('', views.index, name='index'),
   path('doctor', views.doc, name='doc'),
   path('doctor_info/<id>', views.doctor_info, name='doctor_info'),
   path('services', views.services, name='services'),
   path('services_child', views.services_child, name='services_child'),
   path('service/<id>', views.service, name='service'),
   # path('login', views.login_page, name='login'),
   # path('logout', views.logout_page, name='logout'),
   path('login_req', views.login_req, name='login_req'),
   path('reg_req', views.reg_req, name='reg_req'),
   path('apply', views.todoc, name='apply'),
   path('lk', views.lk, name='lk'),
   path('contact', views.contact, name='contact'),
   path('apply/<id>', views.apply, name='apply'),
   path('apply_req', views.apply_req, name='apply_req'),
   path('update_req', views.update_req, name='update_req'),
   path('faq', views.faq, name='faq'),
   # path('edithouse', views.edithouse, name='edithouse'),
   # path('addfilter/<id>', views.addfilter, name='addfilter'),
   # path('addfilter_req', views.addfilter_req, name='addfilter_req'),
   # path('addfav/<id>', views.addfav, name='addfav'),
   # path('delfav/<id>', views.delfav, name='delfav'),
   # path('edit/<id>', views.edit, name='edit'),
   # path('rent/', views.rent, name='rent'),
   # path('about/', views.about, name='about'),
   # path('post/<slug>', views.post, name='post'),



]
