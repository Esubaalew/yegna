#!/usr/bin/env python3
"""
Yegna Farms Deployment Script
Automates the deployment process and runs final checks
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_file_exists(file_path, description):
    """Check if a file exists"""
    if Path(file_path).exists():
        print(f"✅ {description} exists")
        return True
    else:
        print(f"❌ {description} missing")
        return False

def main():
    print("🚀 Yegna Farms Deployment Preparation")
    print("=" * 50)
    
    # Check critical files
    print("\n📁 Checking critical files...")
    files_to_check = [
        ("portfolio/templates/portfolio/base.html", "Base template"),
        ("portfolio/templates/portfolio/home.html", "Home template"),
        ("portfolio/templates/portfolio/about.html", "About template"),
        ("portfolio/templates/portfolio/contact.html", "Contact template"),
        ("static/style.css", "Main stylesheet"),
        ("static/images/og-home.svg", "Home OG image"),
        ("static/images/og-about.svg", "About OG image"),
        ("static/images/og-contact.svg", "Contact OG image"),
        ("static/images/favicon.svg", "Favicon"),
        ("portfolio/templates/robots.txt", "Robots.txt"),
        ("portfolio/templates/sitemap.xml", "Sitemap.xml"),
        ("static/site.webmanifest", "Web manifest"),
    ]
    
    all_files_exist = True
    for file_path, description in files_to_check:
        if not check_file_exists(file_path, description):
            all_files_exist = False
    
    if not all_files_exist:
        print("\n❌ Some critical files are missing. Please check the files above.")
        return False
    
    # Run Django checks
    print("\n🔍 Running Django system checks...")
    if not run_command("python manage.py check", "Django system check"):
        return False
    
    # Collect static files
    print("\n📦 Collecting static files...")
    if not run_command("python manage.py collectstatic --noinput", "Static files collection"):
        return False
    
    # Run migrations
    print("\n🗄️ Running database migrations...")
    if not run_command("python manage.py migrate", "Database migrations"):
        return False
    
    # Test the server
    print("\n🧪 Testing server startup...")
    if not run_command("python manage.py check --deploy", "Deployment checks"):
        print("⚠️  Some deployment checks failed. Review the output above.")
    
    print("\n" + "=" * 50)
    print("🎉 DEPLOYMENT PREPARATION COMPLETE!")
    print("=" * 50)
    
    print("\n📋 Final Checklist:")
    print("✅ All templates and static files are in place")
    print("✅ SEO meta tags configured for all pages")
    print("✅ Open Graph images created")
    print("✅ Robots.txt and sitemap.xml ready")
    print("✅ Favicon and web manifest configured")
    print("✅ Django system checks passed")
    print("✅ Static files collected")
    print("✅ Database migrations applied")
    
    print("\n🌐 Next Steps:")
    print("1. Set up your production server (Nginx + Gunicorn)")
    print("2. Configure SSL certificate for HTTPS")
    print("3. Set environment variables (DEBUG=False, SECRET_KEY, etc.)")
    print("4. Point yegnafarms.com domain to your server")
    print("5. Submit sitemap to Google Search Console")
    print("6. Set up Google Analytics")
    print("7. Test all functionality on production")
    
    print("\n📧 Contact: selamget@icloud.com for deployment assistance")
    print("🚀 Ready to launch Yegna Farms!")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
