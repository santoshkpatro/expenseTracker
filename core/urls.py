from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('credit', views.credit, name='credit'),
    path('debit', views.debit, name='debit'),
    path('delete/<int:id>', views.delete, name='delete')
]