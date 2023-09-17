from django.urls import path
from . import views

urlpatterns = [
    path('program_book/', views.program_book_view, name='program_book'),
]