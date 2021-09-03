from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='register_home'),
    path('new/', views.new_register_view, name='register_new'),
    path('all/', views.all_register_view, name='register_all'),
    
    path('json/ua_empl', views.unassigned_employee_json, name='j_unassigned_employee'),
]