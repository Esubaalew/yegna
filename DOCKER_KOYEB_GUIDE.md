# 🐳 Yegna Farms - Docker + Koyeb Deployment

## 🚀 Quick Deploy (5 Minutes)

### 1. Push to GitHub
```bash
git add .
git commit -m "Ready for Koyeb deployment"
git push origin main
```

### 2. Deploy on Koyeb
1. **Sign up**: [app.koyeb.com](https://app.koyeb.com)
2. **Create App**: Click "Create App"
3. **Connect GitHub**: Select your repository
4. **Configure**:
   - Build Type: **Docker**
   - Port: **8000**
   - Instance: **Nano** (512MB RAM - $5.50/month)

### 3. Environment Variables
In Koyeb dashboard, add:
```
DEBUG=False
SECRET_KEY=your-super-secret-key-make-it-long-and-random-123456789
DJANGO_ALLOWED_HOSTS=yegnafarms.com,www.yegnafarms.com,.koyeb.app
```

### 4. Deploy! 🎉
- Click **"Deploy"**
- Wait 5-10 minutes for build
- Live at: `https://your-app-name.koyeb.app`

---

## 🔧 Local Development

### Run with Docker (Recommended)
```bash
# Build and run with automatic data seeding
docker-compose up --build

# Access at http://localhost:8000
# Admin panel: http://localhost:8000/admin
# Credentials: admin / admin123
```

### Run without Docker
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed database with sample data
python manage.py populate_data
python add_sample_data.py

# Collect static files
python manage.py collectstatic

# Run server
python manage.py runserver
```

## 📊 Database & Sample Data

### Automatic Data Seeding
Your Docker setup automatically handles:
- ✅ **Database migrations**
- ✅ **Sample data seeding** (companies, partnerships, experiences, news)
- ✅ **Admin user creation** (username: admin, password: admin123)
- ✅ **Static file collection**

### Sample Data Includes:
- **Company Info**: Yegna Farms details and contact information
- **9 Partnerships**: UNIDO, ILO, UNICEF, ILRI, etc.
- **6 Experiences**: Major program implementations
- **8 News Articles**: Recent updates and achievements
- **Admin User**: For content management

---

## 🌐 Custom Domain (yegnafarms.com)

### 1. In Koyeb Dashboard
- Go to your app → **Domains**
- Add: `yegnafarms.com`
- Add: `www.yegnafarms.com`

### 2. DNS Settings
Point your domain to Koyeb:
```
Type: CNAME
Name: @
Value: your-app-name.koyeb.app

Type: CNAME
Name: www
Value: your-app-name.koyeb.app
```

### 3. SSL Certificate
- Automatically provided by Koyeb
- HTTPS enabled within 5-10 minutes

---

## 📁 Docker Files Overview

### Core Files:
- ✅ `Dockerfile` - Multi-stage Alpine build
- ✅ `requirements.txt` - Minimal dependencies
- ✅ `docker-compose.yml` - Local development
- ✅ `Procfile` - Koyeb process definition
- ✅ `koyeb.yaml` - Deployment configuration

### Key Features:
- **Multi-stage build** for smaller image size
- **WhiteNoise** for static file serving
- **Alpine Linux** for security and size
- **Environment-based configuration**
- **Production-ready settings**

---

## 🔍 Troubleshooting

### Build Fails?
```bash
# Test locally first
docker build -t yegna-farms .
docker run -p 8000:8000 yegna-farms
```

### App Won't Start?
- Check environment variables in Koyeb dashboard
- Verify `SECRET_KEY` is set
- Check logs in Koyeb app → Logs tab

### Static Files Missing?
- Ensure `python manage.py collectstatic` runs
- Check `STATIC_ROOT` in settings.py
- Verify WhiteNoise is in MIDDLEWARE

---

## 💰 Pricing

### Koyeb Nano Instance
- **RAM**: 512MB
- **CPU**: 0.1 vCPU  
- **Cost**: ~$5.50/month
- **Bandwidth**: 100GB included
- **SSL**: Free
- **Custom Domain**: Free

Perfect for Yegna Farms website! 🌟

---

## ✅ Post-Deployment Checklist

- [ ] App loads at Koyeb URL
- [ ] Custom domain works (if configured)
- [ ] HTTPS certificate active
- [ ] All pages load correctly
- [ ] Contact form works
- [ ] Static files (CSS, images) load
- [ ] Theme toggle works
- [ ] Mobile responsive
- [ ] SEO meta tags present
- [ ] robots.txt accessible: `/robots.txt`
- [ ] sitemap.xml accessible: `/sitemap.xml`

---

## 🎯 SEO Setup

### Google Search Console
1. Add property: `https://yegnafarms.com`
2. Verify ownership
3. Submit sitemap: `https://yegnafarms.com/sitemap.xml`

### Social Media
Your Open Graph images are ready:
- Home: `/static/images/og-home.svg`
- About: `/static/images/og-about.svg`  
- Contact: `/static/images/og-contact.svg`

---

## 🎉 Success!

Your Yegna Farms website is now:
- ✅ **Dockerized** for consistent deployment
- ✅ **Production-ready** with proper settings
- ✅ **SEO-optimized** with meta tags and sitemaps
- ✅ **SSL-secured** with custom domain support
- ✅ **Auto-scaling** on Koyeb platform
- ✅ **Cost-effective** at ~$5.50/month

**Live URL**: `https://yegnafarms.com` 🌟

**Support**: selamget@icloud.com for deployment help!
