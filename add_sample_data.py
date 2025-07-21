#!/usr/bin/env python
"""
Quick script to add more sample data to the Yegna Farms website
Run this after setting up the Django environment
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yegna_portfolio.settings')
django.setup()

from portfolio.models import CompanyInfo, News, Experience, Partnership
from django.contrib.auth import get_user_model

def add_more_partnerships():
    """Add additional partnerships"""
    additional_partnerships = [
        {
            'name': 'Ethiopian Agricultural Transformation Agency (ATA)',
            'description': 'Collaboration on agricultural transformation initiatives and scaling successful farming models across Ethiopia.',
            'mou_signed': True,
            'is_functional': True
        },
        {
            'name': 'World Bank Group',
            'description': 'Partnership for rural development financing and women empowerment programs in agricultural sectors.',
            'mou_signed': False,
            'is_functional': True
        },
        {
            'name': 'African Development Bank',
            'description': 'Support for agricultural value chain development and rural women economic empowerment initiatives.',
            'mou_signed': False,
            'is_functional': True
        }
    ]
    
    for partnership_data in additional_partnerships:
        partnership, created = Partnership.objects.get_or_create(
            name=partnership_data['name'],
            defaults=partnership_data
        )
        if created:
            print(f"✓ Added partnership: {partnership.name}")
        else:
            print(f"- Partnership already exists: {partnership.name}")

def add_more_experiences():
    """Add additional experiences"""
    additional_experiences = [
        {
            'title': 'Women Cooperative Development Program',
            'description': 'Established and supported 15 women cooperatives across rural Ethiopia, providing collective bargaining power and shared resources for poultry farming activities.',
            'partners': 'Local Women Associations, Regional Cooperative Agency',
            'location': 'Multiple regions across Ethiopia',
            'date': '2023-2024'
        },
        {
            'title': 'Youth Employment Initiative',
            'description': 'Extended our model to include young women aged 18-25, creating employment opportunities and preventing rural-urban migration through sustainable agriculture.',
            'partners': 'Ministry of Youth and Sports, UNICEF',
            'location': 'Oromia Region',
            'date': '2024'
        }
    ]
    
    for experience_data in additional_experiences:
        experience, created = Experience.objects.get_or_create(
            title=experience_data['title'],
            defaults=experience_data
        )
        if created:
            print(f"✓ Added experience: {experience.title}")
        else:
            print(f"- Experience already exists: {experience.title}")

def add_more_news():
    """Add additional news items"""
    User = get_user_model()
    admin_user = User.objects.filter(username='admin').first()
    
    if not admin_user:
        print("Admin user not found. Please run populate_data command first.")
        return
    
    additional_news = [
        {
            'title': 'Yegna Farms Model Featured in International Development Conference',
            'content': 'Our innovative women-first approach to agricultural development was featured as a best practice case study at the International Conference on Rural Development in Addis Ababa. The presentation highlighted our success in empowering 216+ women farmers and the scalability of our 100 chicken per household model. International delegates expressed strong interest in replicating our model in other African countries.'
        },
        {
            'title': 'New Training Center Opens in Holeta Processing Hub',
            'content': 'We are proud to announce the opening of our state-of-the-art training center at the Holeta Processing Hub. The facility features modern demonstration areas for poultry husbandry, business management classrooms, and hands-on learning spaces. The center will significantly expand our capacity to train rural women in sustainable farming practices and entrepreneurship skills.'
        },
        {
            'title': 'Partnership with Ethiopian Women Entrepreneurs Association',
            'content': 'Yegna Farms has entered into a strategic partnership with the Ethiopian Women Entrepreneurs Association to provide business development support and market linkage services to our program participants. This collaboration will help women farmers transition from subsistence to commercial farming and develop sustainable business enterprises.'
        }
    ]
    
    for news_data in additional_news:
        news_item, created = News.objects.get_or_create(
            title=news_data['title'],
            defaults={
                'content': news_data['content'],
                'author': admin_user
            }
        )
        if created:
            print(f"✓ Added news: {news_item.title}")
        else:
            print(f"- News already exists: {news_item.title}")

def main():
    print("🐔 Adding additional sample data to Yegna Farms website...")
    print("\n📊 Adding partnerships...")
    add_more_partnerships()
    
    print("\n📈 Adding experiences...")
    add_more_experiences()
    
    print("\n📰 Adding news items...")
    add_more_news()
    
    print("\n✅ Sample data addition complete!")
    print("🌐 Visit http://127.0.0.1:8000 to see the updated website")

if __name__ == "__main__":
    main()
