from django.shortcuts import render
from .models import CompanyInfo, News, Experience, Partnership

# Create your views here.

def home(request):
    company = CompanyInfo.objects.first()
    news = News.objects.order_by('-created_at')[:3]
    return render(request, 'portfolio/home.html', {'company': company, 'news': news})

def about(request):
    company = CompanyInfo.objects.first()
    return render(request, 'portfolio/about.html', {'company': company})

def experiences(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experiences.html', {'experiences': experiences})

def partnerships(request):
    partnerships = Partnership.objects.all()
    return render(request, 'portfolio/partnerships.html', {'partnerships': partnerships})

def news(request):
    news_list = News.objects.order_by('-created_at')
    return render(request, 'portfolio/news.html', {'news_list': news_list})

def contact(request):
    company = CompanyInfo.objects.first()
    return render(request, 'portfolio/contact.html', {'company': company})
