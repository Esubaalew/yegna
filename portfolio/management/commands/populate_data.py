from django.core.management.base import BaseCommand
from portfolio.models import CompanyInfo, News, Experience, Partnership
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the database with sample data for Yegna Farms'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate Yegna Farms data...'))

        # Create or update company info
        company, created = CompanyInfo.objects.get_or_create(
            name="Yegna Farms",
            defaults={
                'motto': "Women First - and it is a women's empowerment program designed to enhance the livelihoods of women in Rural Ethiopia",
                'vision': "To catalyze private-public partnerships for women's empowerment in Ethiopia - Chicken is ATM for women",
                'description': "Yegna Farms is a social enterprise involved in poultry input supplies, educating, and training rural women in poultry husbandry, home economics and saving and credit, implementing the Yegna Farms Model in partnership with public institutions and international institutions.",
                'contact_name': "Selam Getnet",
                'contact_role': "Managing Director",
                'contact_email': "selamget@icloud.com",
                'contact_gender': "Female",
                'contact_languages': "English, Amharic"
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created company info'))
        else:
            self.stdout.write(self.style.WARNING('Company info already exists'))

        # Create partnerships
        partnerships_data = [
            {
                'name': 'UNIDO (United Nations Industrial Development Organization)',
                'description': 'Partnership for industrial development and job creation in Bure Industry Parks command areas through the 100 chicken per household model.',
                'mou_signed': True,
                'is_functional': True
            },
            {
                'name': 'International Labour Organization (ILO)',
                'description': 'Partnership for sustainable poultry farming and livelihood improvement for 216 farmers around Holeta and Sululta.',
                'mou_signed': True,
                'is_functional': True
            },
            {
                'name': 'UNICEF',
                'description': 'Functional partnership focusing on child nutrition and family welfare through sustainable agriculture programs.',
                'mou_signed': True,
                'is_functional': True
            },
            {
                'name': 'ILRI (International Livestock Research Institute)',
                'description': 'Multiple partnerships for research, development, and implementation of sustainable livestock programs with scientific backing.',
                'mou_signed': True,
                'is_functional': True
            },
            {
                'name': 'Oromia Regional Development',
                'description': 'Signed MoU with Oromia Regional Development and ILRI to develop and implement comprehensive development programs and projects across the region.',
                'mou_signed': True,
                'is_functional': True
            },
            {
                'name': 'Ministry of Labor and Skills (MoLS)',
                'description': 'Partnership for the development and implementation of the street chicken frying program in Holeta, Adama, and Hawassa cities.',
                'mou_signed': True,
                'is_functional': True
            },
            {
                'name': 'Holeta City Administration',
                'description': 'Strategic land allocation partnership - 10,000 M² of land allocated for Yegna Farms to build a demonstration and egg and meat processing hub.',
                'mou_signed': True,
                'is_functional': True
            },
            {
                'name': 'Holeta Agricultural Research Institute',
                'description': 'Research partnership providing scientific backing and research-based approaches to poultry farming programs, ensuring best practices and optimal outcomes.',
                'mou_signed': True,
                'is_functional': True
            },
            {
                'name': 'Local Microfinance Institutions',
                'description': 'Developed and implemented functional partnerships with local microfinance institutions to provide financial services, credit access, and savings programs.',
                'mou_signed': True,
                'is_functional': True
            }
        ]

        for partnership_data in partnerships_data:
            partnership, created = Partnership.objects.get_or_create(
                name=partnership_data['name'],
                defaults=partnership_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created partnership: {partnership.name}'))

        # Create experiences
        experiences_data = [
            {
                'title': 'Bure Industry Parks Women Empowerment Program',
                'description': 'Successfully implemented our 100 chicken per household model in partnership with UNIDO, ILRI, and local administration, creating sustainable employment opportunities for farmers in the command areas of Bure Industry Parks in Dangla area.',
                'partners': 'UNIDO, ILRI, Local Administration',
                'location': 'Dangla area, Bure Industry Parks',
                'date': '2023-2024'
            },
            {
                'title': 'Holeta and Sululta Farmers Livelihood Program',
                'description': 'Our flagship program improved the livelihoods of 216 farmers around Holeta and Sululta through comprehensive poultry farming support, training, and market linkage. This program demonstrates the scalability and effectiveness of our model.',
                'partners': 'ILO, ILRI, Holeta Agricultural Research Institute',
                'location': 'Holeta and Sululta',
                'date': '2022-2024'
            },
            {
                'title': 'Street Chicken Frying Urban Employment Program',
                'description': 'Partnered with the Ministry of Labor and Skills (MoLS) to develop and implement an innovative street chicken frying program, creating urban employment opportunities and expanding market access for rural producers.',
                'partners': 'Ministry of Labor and Skills (MoLS)',
                'location': 'Holeta, Adama, Hawassa cities',
                'date': '2023-2024'
            }
        ]

        for experience_data in experiences_data:
            experience, created = Experience.objects.get_or_create(
                title=experience_data['title'],
                defaults=experience_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created experience: {experience.title}'))

        # Create news items
        news_data = [
            {
                'title': 'Yegna Farms Expands Partnership Network with UNIDO',
                'content': 'We are excited to announce the expansion of our partnership with UNIDO (United Nations Industrial Development Organization) to implement our proven 100 chicken per household model in the Bure Industry Parks command areas. This partnership will create decent jobs for farmers and integrate rural communities with industrial development initiatives, demonstrating the scalability of our women-first approach to agricultural empowerment.'
            },
            {
                'title': '216 Women Farmers Successfully Empowered in Holeta-Sululta Program',
                'content': 'Our flagship program in partnership with ILO, ILRI, and Holeta Agricultural Research Institute has successfully empowered 216 women farmers around Holeta and Sululta. Each participant received 100 carefully selected chickens, comprehensive training, and ongoing support. The program has resulted in significant improvements in household income, nutrition security, and women\'s economic independence. Participants are now saving an average of 2,000 Birr per month through our structured savings program.'
            },
            {
                'title': 'Holeta City Allocates 10,000 M² for Processing Hub Development',
                'content': 'In a major milestone for Yegna Farms, Holeta City Administration has allocated 10,000 square meters of land for the development of our demonstration and egg and meat processing hub. This facility will serve as a center of excellence for poultry farming training, value addition activities, and market linkage services. The processing hub will significantly enhance our capacity to support more women farmers and create additional employment opportunities in the value chain.'
            },
            {
                'title': 'Street Chicken Frying Program Launches in Three Cities',
                'content': 'Our innovative street chicken frying program, developed in partnership with the Ministry of Labor and Skills, has officially launched in Holeta, Adama, and Hawassa cities. This urban employment initiative creates market opportunities for rural chicken producers while providing affordable, nutritious food options in urban areas. The program demonstrates our commitment to creating comprehensive value chains that benefit both rural producers and urban consumers.'
            },
            {
                'title': 'Research Partnership with ILRI Yields Breakthrough Results',
                'content': 'Our ongoing research partnership with the International Livestock Research Institute (ILRI) has yielded significant breakthroughs in optimizing chicken breeds for Ethiopian conditions. The research has identified the most productive and resilient chicken varieties that thrive in local environments while maximizing egg production. These findings are being integrated into our training programs to ensure all participating women receive the highest quality chickens for maximum impact.'
            }
        ]

        # Get or create a user for news authorship
        User = get_user_model()
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@yegnafarms.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user'))

        for news_item_data in news_data:
            news_item, created = News.objects.get_or_create(
                title=news_item_data['title'],
                defaults={
                    'content': news_item_data['content'],
                    'author': admin_user
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created news item: {news_item.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated Yegna Farms data!'))
        self.stdout.write(self.style.SUCCESS('You can now view the website with dynamic content.'))
        self.stdout.write(self.style.SUCCESS('Admin credentials: username=admin, password=admin123'))
