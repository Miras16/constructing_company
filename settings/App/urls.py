
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signin/', views.login,name='login'),
    path('signup/', views.register,name='register'),
    path('about/', views.about,name='about'),
    path('faq/', views.FAQ,name='faq'),
    path('news-right-sidebar/',views.news_right, name='news_right'),
    path('pricing/', views.pricing, name='pricing'),
    path('projects/',views.projects, name='projects'),
    path('services/',views.services, name='services'),
    path('team/',views.team, name='team'),
    path('testimonials/',views.testimon, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),
]