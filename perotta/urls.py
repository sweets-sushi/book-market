from django.urls import path
from . import views

app_name = 'perotta'

urlpatterns = [
    path('', views.TemplateView.as_view(), name='landing'),
    path('home/', views.IndexView.as_view(), name='index'),
    path('add/', views.add, name='add'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),

]
