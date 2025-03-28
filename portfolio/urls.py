# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<slug:project_slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
]