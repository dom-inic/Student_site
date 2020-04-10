from django.urls import path
from . import views

urlpatterns = [
    path('learning_log/topics/', views.topics, name="topics"), 
    
]
