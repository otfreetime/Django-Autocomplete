from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='page'),
    path('email_autocomplete/', views.email_autocomplete, name='email_autocomplete')

]