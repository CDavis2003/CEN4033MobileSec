from django.urls import path
from . import views

urlpatterns = [
    path('add-question/', views.add_question, name='add_question'),
    path('success/', views.success, name='success'),
]

