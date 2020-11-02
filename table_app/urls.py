from . import views
from django.urls import path


urlpatterns = [
    path('table-list', views.tableList, name='table-list'),
    path('table-create', views.tableCreate, name='table-create'),
    path('table-update/<int:id>', views.tableUpdate, name='table-update'),
    path('table-delete/<int:id>', views.tableDelete, name = 'table-delete'),

]
