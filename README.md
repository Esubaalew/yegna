# 🐔 Yegna Farms - Growing Food. Growing Futures.

A stunning, modern website for Yegna Farms, a social enterprise dedicated to empowering women through sustainable poultry farming in rural Ethiopia.

## 🌟 Features

### ✨ **Modern Design**
- **Beautiful SVG Graphics**: Custom-designed rooster logo and agricultural icons
- **Responsive Layout**: Perfect on desktop, tablet, and mobile devices
- **Professional Color Scheme**: Green, orange, and yellow palette reflecting agriculture and growth
- **Smooth Animations**: Floating elements, hover effects, and transitions
- **Custom Patterns**: Ethiopian-inspired background patterns and textures

### 📊 **Dynamic Content Management**
- **Django Admin Interface**: Easy content management for non-technical users
- **Company Information**: Editable company details, contact info, and mission
- **News Management**: Add, edit, and publish news articles and updates
- **Partnership Tracking**: Manage partnerships with MOU status and functionality
- **Experience Documentation**: Showcase impact stories and program results

### 🎨 **Visual Excellence**
- **Custom SVG Icons**: Hand-crafted icons for chickens, training, money, houses, eggs, partnerships, and more
- **Gradient Effects**: Beautiful color transitions and text effects
- **Professional Typography**: Google Fonts (Inter + Playfair Display)
- **Enhanced Cards**: Hover effects, shadows, and interactive elements
- **Background Patterns**: Subtle agricultural and empowerment-themed patterns

### 📱 **User Experience**
- **Intuitive Navigation**: Clear menu structure with active page indicators
- **Mobile-First Design**: Responsive hamburger menu and touch-friendly interface
- **Fast Loading**: Optimized SVG graphics and efficient CSS
- **Accessibility**: Semantic HTML and proper contrast ratios

## 🚀 **Pages Overview**

### 🏠 **Home Page**
- Hero section with animated rooster icon
- Impact statistics with custom SVG icons
- Yegna Farms model overview
- Partnership highlights
- Latest news section
- Call-to-action sections

### ℹ️ **About Page**
- Mission and vision showcase
- Detailed model components with icons
- Impact goals visualization
- Professional layout with floating animations

### 📈 **Experiences Page**
- Success stories with visual timelines
- Measurable impact statistics
- Key partnership highlights
- Program outcomes and metrics

### 🤝 **Partnerships Page**
- Comprehensive partner showcase
- Organized by category (International, Government, Financial, Research)
- Partnership benefits and network visualization
- Dynamic partnership status tracking

### 📰 **News Page**
- Modern article layout with enhanced typography
- Publication dates and author information
- Related content suggestions
- Newsletter signup integration

### 📞 **Contact Page**
- Professional contact information
- Partnership opportunities
- Facility details and location
- Quick contact options

## 🛠️ **Technical Stack**

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JavaScript
- **Graphics**: Custom SVG illustrations and icons
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Styling**: CSS Grid, Flexbox, Custom Properties
- **Fonts**: Google Fonts (Inter, Playfair Display)

## 📦 **Installation & Setup**

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd yegna
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows
   # or
   source .venv/bin/activate      # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Populate sample data**
   ```bash
   python manage.py populate_data
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the website**
   Open http://127.0.0.1:8000 in your browser

## 👨‍💼 **Admin Access**

- **URL**: http://127.0.0.1:8000/admin/
- **Username**: admin
- **Password**: admin123

## 📊 **Sample Data Included**

### 🏢 **Company Information**
- Complete Yegna Farms profile
- Contact details for Selam Getnet (Managing Director)
- Mission, vision, and motto

### 🤝 **Partnerships**
- UNIDO, ILO, UNICEF, ILRI
- Government partnerships (Oromia Regional Development, Ministry of Labor)
- Financial institutions and research partners

### 📈 **Experiences**
- Bure Industry Parks program
- Holeta-Sululta farmers program (216 women empowered)
- Street chicken frying urban program

### 📰 **News Articles**
- Partnership announcements
- Program success stories
- Facility developments
- Research breakthroughs

## 🎨 **Customization**

### **Adding New Icons**
1. Edit `static/icons.svg` or `portfolio/templates/portfolio/icons.html`
2. Add new `<symbol>` elements with unique IDs
3. Use in templates with `<svg><use href="#icon-id"/></svg>`

### **Updating Colors**
1. Edit CSS variables in `static/style.css`
2. Modify the `:root` section with new color values
3. Colors automatically update throughout the site

### **Adding Content**
1. Use Django Admin interface at `/admin/`
2. Add partnerships, experiences, news articles
3. Update company information as needed

## 🌍 **Impact Metrics**

The website showcases Yegna Farms' impressive impact:
- **216+ women empowered** through poultry farming programs
- **100 chickens per woman** providing sustainable income
- **2,000 Birr monthly savings** per household
- **5+ international partnerships** with UN agencies and research institutions
- **3 cities** implementing street chicken frying programs
- **10,000 M²** processing hub facility in Holeta

## 🚀 **Future Enhancements**

- **Multi-language Support**: Amharic translation
- **Interactive Maps**: Show program locations
- **Success Stories**: Individual farmer testimonials
- **Photo Gallery**: Program images and facility photos
- **Blog System**: Regular updates and insights
- **Newsletter Integration**: Email subscription management

## 📞 **Contact**

**Yegna Farms**
- **Managing Director**: Selam Getnet
- **Email**: selamget@icloud.com
- **Location**: Holeta, Ethiopia
- **Languages**: English, Amharic

---

**"Women First - Transforming lives through sustainable poultry farming in rural Ethiopia"**

🐔 **Chicken is ATM for women** - Creating employment, wealth creation, poverty reduction, and nutrition security.
