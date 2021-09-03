from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='accounts_home'),
    path('billDesk', views.bill_desk_view, name='accounts_bill_desk'),
    path('accounting', views.acc_desk_view, name='accounts_bal_desk'),
    ###jax for billDesk
    path('billDesk/jax/ts', views.billDesk_tools_jax, name='accounts_jax_billDesk_tools'),
    path('billDesk/jax/nb', views.billDesk_new_bill_jax, name='accounts_jax_billDesk_newBill'),
    path('billDesk/jax/bl', views.billDesk_bill_info_jax, name='accounts_jax_bill_info'),
    
]