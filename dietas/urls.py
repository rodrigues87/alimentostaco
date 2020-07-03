from django.contrib import admin
from django.urls import path
from dietas.views import *


urlpatterns = [
    path('', list_dietas, name='list_dietas'),
    path('minhas_dietas/', list_minhas_dietas, name='list_dietas'),

    path('create', create_dieta, name='create_dieta'),
    path('update/<int:id>', update_dieta, name='update_dieta'),
    path('delete/<int:id>', delete_dieta, name='delete_dieta'),

]
