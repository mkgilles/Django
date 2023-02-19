from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='dashboard_index'),
    path('home/', views.dashboard_home, name='dashboard_home'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('products/', views.product_list, name='dashboard_product_list'),
    path('sales/', views.sale_list, name='dashboard_sale_list')

]
