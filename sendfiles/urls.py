from django.urls import path
from . import views

urlpatterns = [
    path('api/template/<str:name>/', views.get_svelte_page, name='get_svelte_page'),
]
