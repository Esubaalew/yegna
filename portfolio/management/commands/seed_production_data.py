from django.core.management.base import BaseCommand
from django.core.management import call_command
from portfolio.models import CompanyInfo, Partnership, Experience, News
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Seed production database with initial data if empty'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force seeding even if data exists',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🌱 Checking production database...'))

        # Check if database has data
        company_count = CompanyInfo.objects.count()
        partnership_count = Partnership.objects.count()
        experience_count = Experience.objects.count()
        news_count = News.objects.count()
        user_count = get_user_model().objects.count()

        has_data = any([company_count, partnership_count, experience_count, news_count])

        if has_data and not options['force']:
            self.stdout.write(
                self.style.WARNING(
                    f'📊 Database already has data:\n'
                    f'  - Companies: {company_count}\n'
                    f'  - Partnerships: {partnership_count}\n'
                    f'  - Experiences: {experience_count}\n'
                    f'  - News: {news_count}\n'
                    f'  - Users: {user_count}\n'
                    f'Use --force to seed anyway.'
                )
            )
            return

        self.stdout.write(self.style.SUCCESS('🌱 Seeding production database...'))

        # Run the main populate_data command
        self.stdout.write('📊 Running populate_data command...')
        call_command('populate_data')

        # Run additional sample data script if it exists
        if os.path.exists('add_sample_data.py'):
            self.stdout.write('📊 Adding additional sample data...')
            try:
                import subprocess
                result = subprocess.run(['python', 'add_sample_data.py'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    self.stdout.write(self.style.SUCCESS('✅ Additional sample data added'))
                else:
                    self.stdout.write(self.style.WARNING(f'⚠️ Additional sample data script had issues: {result.stderr}'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠️ Could not run additional sample data: {e}'))

        # Final count
        final_company_count = CompanyInfo.objects.count()
        final_partnership_count = Partnership.objects.count()
        final_experience_count = Experience.objects.count()
        final_news_count = News.objects.count()
        final_user_count = get_user_model().objects.count()

        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Production database seeded successfully!\n'
                f'  - Companies: {final_company_count}\n'
                f'  - Partnerships: {final_partnership_count}\n'
                f'  - Experiences: {final_experience_count}\n'
                f'  - News: {final_news_count}\n'
                f'  - Users: {final_user_count}\n'
                f'🌐 Your Yegna Farms website is ready!'
            )
        )

        # Show admin credentials if admin user was created
        admin_user = get_user_model().objects.filter(username='admin').first()
        if admin_user:
            self.stdout.write(
                self.style.SUCCESS(
                    '👤 Admin credentials:\n'
                    '   Username: admin\n'
                    '   Password: admin123\n'
                    '   Email: admin@yegnafarms.com'
                )
            )
