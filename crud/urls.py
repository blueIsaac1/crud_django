from django.urls import path
from .views import home, contactlist, forms, contact_create, contact_delete, contact_update

urlpatterns = [
    path('', home, name='home'),
    path('forms/', forms, name='forms'),
    path('contactlist/', contactlist, name='contactlist'),
    path('contact_create/', contact_create, name='contact_create'),
    path('contact_delete/<int:pk>/', contact_delete, name='contact_delete'),
    path('contact_update/<int:pk>/', contact_update, name='contact_update'),
]
