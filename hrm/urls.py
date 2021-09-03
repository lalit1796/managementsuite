from django.urls import path

from . import views

urlpatterns = [

    path('', views.index_view, name='hrm_home'),
    
    path('employee', views.employee_view, name='hrm_employee'),
    path('employee/add-new-employee/', views.employee_new_add_view, name='hrm_addNewEmployee'),
    path('employee/<int:id>/', views.employee_profile_view, name='hrm_employeeProfile'),
    ##jax for employee
    path('employee/jax/<int:id>/bs', views.employee_profile_basic_jax, name='hrm_jax_employee_basic'),
    path('employee/jax/<int:id>/em', views.employee_profile_emergency_jax, name='hrm_jax_employee_emergency'),
    path('employee/jax/<int:id>/fa', views.employee_profile_family_jax, name='hrm_jax_employee_family'),
    path('employee/jax/<int:id>/ee', views.employee_profile_employement_jax, name='hrm_jax_employee_employement'),
    path('employee/jax/<int:id>/nm', views.employee_profile_nominee_jax, name='hrm_jax_employee_nominee'),
    path('employee/jax/<int:id>/dc', views.employee_profile_documents_jax, name='hrm_jax_employee_documents'),
    path('employee/jax/<int:id>/jb', views.employee_profile_job_jax, name='hrm_jax_employee_job'),
    
    
    path('recruit/', views.recruit_view, name='hrm_recruit'),
    
    path('recruit/hire/', views.recruit_hire_view, name='hrm_recruit_hire'),
    path('recruit/hire/<slug:code>/', views.recruit_hire_code_view, name='hrm_recruit_hire_code'),
    
    path('recruit/jobs/', views.recruit_vacancy_view, name='hrm_recruit_vacancy'),
    path('recruit/jobs/new/', views.recruit_vacancy_new_view, name='hrm_recruit_vacancy_new'),
    
    ##jax for recruit
    path('recruit/jax/candidates/', views.recruit_hire_code_candidates_jax, name='hrm_jax_rec_cand'),
    path('recruit/jax/new-candidates/', views.recruit_hire_code_newcandidates_jax, name='hrm_jax_rec_add'),
    path('recruit/jax/stats/', views.recruit_hire_code_stats_jax, name='hrm_jax_rec_stats'),
    path('recruit/jax/edit/', views.recruit_hire_code_edit_jax, name='hrm_jax_rec_edit'),
    
    path('payroll/', views.payroll_view, name='hrm_payroll'),
    path('payroll/slug/', views.create_paysheet_view, name='hrm_paysheet'), 
    
    
    
    path('training/', views.training_view, name='hrm_training'),
    path('file/', views.file_view, name='hrm_file'),
    path('report/', views.report_view, name='hrm_report'),
    
    #jax
    path('hrm/jax/empl/', views.empl_code_data_jax, name='hrm_jax_empl_code')
    
    
    
]
