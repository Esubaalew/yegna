from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experiences/', views.experiences, name='experiences'),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),

    # SEO URLs
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml'), name='sitemap'),
]