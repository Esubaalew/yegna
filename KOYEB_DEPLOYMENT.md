# 🚀 Yegna Farms - Koyeb Docker Deployment Guide

## 🎯 Quick Deploy (5 Minutes)

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Ready for Koyeb deployment"
git push origin main
```

### Step 2: Deploy on Koyeb
1. Go to [app.koyeb.com](https://app.koyeb.com)
2. Click "Create App"
3. Choose "GitHub" and select your repository
4. Configure:
   - **Build Type**: Docker
   - **Port**: 8000
   - **Instance**: Nano (512MB RAM)

### Step 3: Environment Variables
Add these in Koyeb dashboard:
```
DEBUG=False
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
DJANGO_ALLOWED_HOSTS=yegnafarms.com,www.yegnafarms.com,.koyeb.app
```

### Step 4: Deploy & Go Live! 🎉
- Click "Deploy"
- Wait 5-10 minutes
- Your site will be live at `https://your-app-name.koyeb.app`

---

## 📋 Prerequisites

1. **Koyeb Account**: Sign up at [koyeb.com](https://www.koyeb.com)
2. **GitHub Repository**: Push your code to GitHub
3. **Domain**: yegnafarms.com (optional, Koyeb provides free subdomain)

## 🐳 Docker Files Overview

### Core Files Created:
- ✅ `Dockerfile` - Multi-stage production build
- ✅ `requirements.txt` - Python dependencies
- ✅ `docker-compose.yml` - Local development
- ✅ `koyeb.yaml` - Koyeb configuration
- ✅ `entrypoint.sh` - Deployment automation
- ✅ `nginx.conf` - Reverse proxy config
- ✅ `.dockerignore` - Optimize build context

## 🚀 Deployment Methods

### Method 1: Koyeb Web Interface (Recommended)

1. **Login to Koyeb Dashboard**
   - Go to [app.koyeb.com](https://app.koyeb.com)
   - Sign in with your account

2. **Create New App**
   - Click "Create App"
   - Choose "GitHub" as source
   - Connect your GitHub repository

3. **Configure Build Settings**
   ```
   Build Type: Docker
   Dockerfile: Dockerfile
   Build Context: /
   ```

4. **Environment Variables**
   ```
   DEBUG=False
   SECRET_KEY=your-super-secret-key-here
   DJANGO_SETTINGS_MODULE=yegna_portfolio.settings
   ALLOWED_HOSTS=yegnafarms.com,www.yegnafarms.com,.koyeb.app
   DATABASE_URL=sqlite:///db.sqlite3
   SECURE_SSL_REDIRECT=True
   ```

5. **Instance Configuration**
   ```
   Instance Type: Nano (512MB RAM, 0.1 vCPU)
   Region: Frankfurt (fra) or closest to your users
   Port: 8000
   Health Check: /
   ```

6. **Deploy**
   - Click "Deploy"
   - Wait for build and deployment (5-10 minutes)

### Method 2: Koyeb CLI

1. **Install Koyeb CLI**
   ```bash
   # macOS
   brew install koyeb/tap/koyeb
   
   # Linux/Windows
   curl -fsSL https://cli.koyeb.com/install.sh | sh
   ```

2. **Login**
   ```bash
   koyeb login
   ```

3. **Deploy with Configuration File**
   ```bash
   koyeb app deploy --config koyeb.yaml
   ```

## 🔧 Local Development with Docker

### Quick Start
```bash
# Build and run locally
docker-compose up --build

# Access at http://localhost:8000
```

### Individual Commands
```bash
# Build the image
docker build -t yegna-farms .

# Run container
docker run -p 8000:8000 \
  -e DEBUG=True \
  -e SECRET_KEY=dev-secret-key \
  yegna-farms

# Run with database
docker-compose up db -d
docker run -p 8000:8000 \
  --link yegna-farms_db_1:db \
  -e DATABASE_URL=postgres://postgres:postgres@db:5432/yegna_farms \
  yegna-farms
```

## 🌐 Custom Domain Setup

### 1. In Koyeb Dashboard
- Go to your app settings
- Click "Domains"
- Add custom domain: `yegnafarms.com`
- Add www redirect: `www.yegnafarms.com`

### 2. DNS Configuration
Point your domain to Koyeb:
```
Type: CNAME
Name: @
Value: [your-app-name].koyeb.app

Type: CNAME  
Name: www
Value: [your-app-name].koyeb.app
```

### 3. SSL Certificate
- Koyeb automatically provides SSL certificates
- HTTPS will be enabled within 5-10 minutes

## 📊 Environment Variables for Production

### Required Variables
```bash
DEBUG=False
SECRET_KEY=your-super-secret-key-generate-new-one
DJANGO_SETTINGS_MODULE=yegna_portfolio.settings
ALLOWED_HOSTS=yegnafarms.com,www.yegnafarms.com,.koyeb.app
```

### Optional Variables
```bash
# Database (if using external DB)
DATABASE_URL=postgres://user:pass@host:port/dbname

# Email (for contact form)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@yegnafarms.com

# Security
SECURE_SSL_REDIRECT=True
DJANGO_LOG_LEVEL=INFO
```

## 🔍 Monitoring & Debugging

### View Logs
```bash
# Koyeb CLI
koyeb logs [app-name]

# Or in Koyeb dashboard
# Go to your app > Logs tab
```

### Health Checks
- Endpoint: `https://yegnafarms.com/`
- Expected: HTTP 200 response
- Timeout: 10 seconds
- Interval: 30 seconds

### Performance Monitoring
- CPU usage: Monitor in Koyeb dashboard
- Memory usage: 512MB limit on Nano instance
- Response time: Should be < 2 seconds

## 💰 Pricing Estimate

### Koyeb Nano Instance
- **RAM**: 512MB
- **CPU**: 0.1 vCPU
- **Cost**: ~$5.50/month
- **Bandwidth**: 100GB included
- **SSL**: Free
- **Custom Domain**: Free

### Scaling Options
- **Micro**: 1GB RAM, 0.25 vCPU (~$11/month)
- **Small**: 2GB RAM, 0.5 vCPU (~$22/month)
- **Auto-scaling**: Available on all plans

## 🚨 Troubleshooting

### Common Issues

1. **Build Fails**
   ```bash
   # Check Dockerfile syntax
   docker build -t test .
   
   # Check requirements.txt
   pip install -r requirements.txt
   ```

2. **App Won't Start**
   ```bash
   # Check logs in Koyeb dashboard
   # Verify environment variables
   # Check Django settings
   ```

3. **Static Files Not Loading**
   ```bash
   # Verify STATIC_ROOT in settings
   # Check WhiteNoise configuration
   # Ensure collectstatic runs in entrypoint.sh
   ```

4. **Database Issues**
   ```bash
   # Check DATABASE_URL format
   # Verify migrations run in entrypoint.sh
   # Consider using external PostgreSQL
   ```

## 🎯 Post-Deployment Checklist

- [ ] App loads at your Koyeb URL
- [ ] Custom domain works (if configured)
- [ ] HTTPS certificate is active
- [ ] All pages load correctly
- [ ] Contact form works
- [ ] Static files (CSS, images) load
- [ ] SEO meta tags are present
- [ ] robots.txt accessible
- [ ] sitemap.xml accessible
- [ ] Mobile responsive design works
- [ ] Dark/light theme toggle works

## 📈 SEO & Analytics Setup

### Google Search Console
1. Add property: `https://yegnafarms.com`
2. Verify ownership via HTML tag
3. Submit sitemap: `https://yegnafarms.com/sitemap.xml`

### Google Analytics
Add to base template:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🎉 Success!

Your Yegna Farms website is now:
- ✅ Deployed on Koyeb with Docker
- ✅ Optimized for production
- ✅ SEO-ready with meta tags and sitemaps
- ✅ SSL-secured with custom domain
- ✅ Auto-scaling capable
- ✅ Monitoring enabled

**Live URL**: `https://yegnafarms.com` 🌟

**Support**: Contact selamget@icloud.com for any deployment assistance!
