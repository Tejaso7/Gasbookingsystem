from django.urls import path
from . import views
urlpatterns = [

    path('h/',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('d/',views.signupform,name='signup'),
    path('',views.mainpage,name='main'),
    path('service/',views.service,name='service'),
    path('client/',views.client,name='client'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('justbefore/', views.justbefore, name='justbefore'),
    path('clientafterlogin/', views.clientafterlogin, name='clientafterlogin'),
    path('adminafterlogin/', views.adminafterlogin, name='adminafterlogin'),
    path('save_admin/', views.save_admin, name='save_admin'),
    path('save_client/', views.save_client, name='save_client'),
    path('client_list/', views.client_list, name='client_list'),
    # path('client_data/<int:pk>', views.client_data, name='client_data'),
    path('admin_list/', views.admin_list, name='admin_list'),
    # path('admin_data/<int:pk>', views.admin_data, name='admin_data'),
    path('choice/', views.choice, name='choice'),
    path('reg_admin/', views.reg_admin, name='reg_admin'),
    path('reg_client/', views.reg_client, name='reg_client'),
    path('log_admin/', views.log_admin, name='log_admin'),
    path('log_client/', views.log_client, name='log_client'),


]
