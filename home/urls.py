from django.urls import path
from . import views
urlpatterns= [
    path('', views.home_view, name='home'),
    path('chat/<int:document_id>/', views.chat_view, name='chat'),
    path('delete/<int:document_id>/', views.delete_pdf, name="delete_pdf")
]