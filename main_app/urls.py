from django.urls import path, URLPattern
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/', views.jobs_index, name='jobs'),
    path('jobs/<int:job_id>/', views.job_detail, name='detail'),
    path('jobs/create', views.JobCreate.as_view(), name='jobs_create'),
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
    path('jobs/<int:job_id>/add_event', views.add_event, name='add_event'),

    path('companies/', views.CompanyList.as_view(), name='companies_index'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='companies_detail'),
    path('companies/create/', views.CompanyCreate.as_view(), name='companies_create'),
    path('companies/<int:pk>/update/', views.CompanyUpdate.as_view(), name='companies_update'),
    path('companies/<int:pk>/delete', views.CompanyDelete.as_view(), name='companies_delete'),

    path('jobs/<int:job_id>/assoc_company/<int:company_id>/', views.assoc_company, name = 'assoc_company'),
    path('jobs/<int:job_id>/unassoc_company/<int:company_id>/', views.unassoc_company, name = 'unassoc_company'),
    path('accounts/signup/', views.signup, name='signup')



]
