from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('cbt/', views.chatbot, name='chatbot'),
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('handleLogout/', views.handleLogout, name='handleLogout'),
    path('simplify/', views.simplify, name='simplify'),
    path('simplifyDoc/', views.legal_document_view, name='legal_document_view'),
    path('slot_booking/', views.slot_booking, name="slot_booking"),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('slot_booking_form/', views.slot_booking_form, name='slot_booking_form')]