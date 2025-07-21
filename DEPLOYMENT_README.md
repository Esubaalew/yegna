# Yegna Farms - Deployment Guide

## 🚀 Production Deployment Checklist

### 1. Domain Configuration
- **Domain**: yegnafarms.com
- **SSL Certificate**: Ensure HTTPS is enabled
- **DNS Settings**: Point to your hosting provider

### 2. Django Settings for Production

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yegnafarms.com', 'www.yegnafarms.com']

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
```

### 3. SEO & Performance Features ✅

#### **Meta Tags & Open Graph**
- ✅ Comprehensive meta tags for all pages
- ✅ Open Graph images for social sharing
- ✅ Twitter Card optimization
- ✅ Structured data (JSON-LD) for search engines

#### **Technical SEO**
- ✅ robots.txt configured
- ✅ XML sitemap with all pages
- ✅ Canonical URLs for all pages
- ✅ Proper heading hierarchy (H1, H2, H3)
- ✅ Alt text for all images
- ✅ Semantic HTML structure

#### **Performance Optimizations**
- ✅ CSS optimizations and minification ready
- ✅ Font loading optimizations
- ✅ Smooth scrolling enabled
- ✅ Box-sizing optimizations
- ✅ Responsive images and SVG icons

#### **Accessibility**
- ✅ Skip links for screen readers
- ✅ ARIA labels and roles
- ✅ Proper color contrast ratios
- ✅ Keyboard navigation support

### 4. Static Files Structure

```
static/
├── style.css (optimized)
├── images/
│   ├── og-home.svg (1200x630 Open Graph)
│   ├── og-about.svg (1200x630 Open Graph)
│   ├── og-contact.svg (1200x630 Open Graph)
│   ├── favicon.svg
│   ├── apple-touch-icon.svg
│   └── ...
├── robots.txt
├── sitemap.xml
└── site.webmanifest
```

### 5. Pre-Deployment Commands

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser (if needed)
python manage.py createsuperuser

# Test the application
python manage.py runserver
```

### 6. Server Configuration

#### **Nginx Configuration Example**
```nginx
server {
    listen 80;
    server_name yegnafarms.com www.yegnafarms.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yegnafarms.com www.yegnafarms.com;
    
    # SSL configuration
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    
    # Static files
    location /static/ {
        alias /path/to/staticfiles/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # SEO files
    location = /robots.txt {
        alias /path/to/staticfiles/robots.txt;
    }
    
    location = /sitemap.xml {
        alias /path/to/staticfiles/sitemap.xml;
    }
    
    # Django application
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 7. Environment Variables

```bash
# .env file
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yegnafarms.com,www.yegnafarms.com
DATABASE_URL=your-database-url
```

### 8. Post-Deployment Verification

#### **SEO Checklist**
- [ ] Test robots.txt: `https://yegnafarms.com/robots.txt`
- [ ] Test sitemap: `https://yegnafarms.com/sitemap.xml`
- [ ] Verify Open Graph images load correctly
- [ ] Test social media sharing (Facebook, Twitter, LinkedIn)
- [ ] Submit sitemap to Google Search Console
- [ ] Submit sitemap to Bing Webmaster Tools

#### **Performance Testing**
- [ ] Google PageSpeed Insights
- [ ] GTmetrix performance test
- [ ] Mobile-friendly test
- [ ] Core Web Vitals check

#### **Functionality Testing**
- [ ] All pages load correctly
- [ ] Contact form works
- [ ] Theme toggle (light/dark) functions
- [ ] Responsive design on all devices
- [ ] All icons and images display properly

### 9. Analytics & Monitoring

Add these to your base template before deployment:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>

<!-- Google Search Console -->
<meta name="google-site-verification" content="your-verification-code" />
```

### 10. Social Media Setup

Create accounts and link them:
- Facebook: facebook.com/yegnafarms
- Twitter: twitter.com/yegnafarms  
- LinkedIn: linkedin.com/company/yegnafarms

### 🎉 Ready for Launch!

Your Yegna Farms website is now fully optimized for:
- ✅ Search Engine Optimization (SEO)
- ✅ Social Media Sharing
- ✅ Performance & Speed
- ✅ Accessibility
- ✅ Mobile Responsiveness
- ✅ Professional Appearance

**Contact**: selamget@icloud.com for any deployment assistance.
