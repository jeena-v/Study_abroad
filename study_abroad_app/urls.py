from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about/', views.about, name='about'),
    path('blog',views.blog,name='blog'),
    path('courses',views.courses,name='courses'),
    path('counsellors/', views.counsellor_form, name='counsellors'),
    path('counselling-popup/', views.counselling_popup, name='counselling_popup'),
    path('blogs/', views.blog_list, name='blog'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search_view, name='search'),
    path('about-details/', views.about_details, name='about-details'),
    
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),

    path('study-abroad/<slug:slug>/', views.country_detail, name='country_detail'),












    







]