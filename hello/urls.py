from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddView.as_view(), name='add'),
    path('list', views.ListView.as_view(), name='list'),

]