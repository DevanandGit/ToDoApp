from django.urls import path
from .views import AddCreateView, viewListView, DeleteactivityDeleteView, UpdateActivityUpdateView


app_name = 'app1'

urlpatterns = [
    path('addnew/', AddCreateView.as_view(), name = 'addnew'),
    path('view/', viewListView.as_view(), name='view'),
    path('delete/<int:pk>', DeleteactivityDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateActivityUpdateView.as_view(), name='update'),
]
