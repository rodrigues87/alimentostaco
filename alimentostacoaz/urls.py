from django.contrib import admin
from django.urls import path
from alimentostacoaz.views import *

urlpatterns = [
    path('', list_alimentos, name='list_alimentos'),
    path('list_meus_alimentos/', list_meus_alimentos, name='list_meus_alimentos'),
    path('create', create_alimento, name='create_alimento'),
    path('update/<int:id>', update_alimento, name='update_alimento'),
    path('delete/<int:id>', delete_alimento, name='delete_alimento'),
    path('add_alimento_dieta/<int:id_alimento>/<int:id_dieta>',add_alimento_dieta,name ='add_alimento_dieta')
]
