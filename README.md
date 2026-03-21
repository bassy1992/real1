# BELLEROCK Holdings - Luxury Real Estate Platform

A full-stack luxury real estate platform featuring property listings, investment opportunities, and comprehensive property management.

## 🏗️ Tech Stack

### Backend
- **Django 4.2.29** - Python web framework
- **Django REST Framework** - API development
- **Django Unfold** - Modern admin interface
- **DigitalOcean Spaces** - Cloud storage for media files
- **SQLite** - Database (development)

### Frontend
- **React 18** with TypeScript
- **Vite** - Build tool
- **React Router** - Navigation
- **Tailwind CSS** - Styling

## 📁 Project Structure

```
.
├── back/                          # Django backend
│   ├── backend/                   # Main Django project
│   ├── properties/                # Property management app
│   ├── investment_opportunities/  # Investment management app
│   ├── media/                     # Local media files (gitignored)
│   ├── staticfiles/              # Collected static files
│   └── requirements.txt          # Python dependencies
│
└── front/                        # React frontend
    ├── src/
    │   ├── components/          # Reusable components
    │   ├── pages/              # Page components
    │   ├── services/           # API services
    │   └── types/              # TypeScript types
    ├── package.json
    └── vite.config.ts
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- pip
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd back
```

2. Install Python dependencies:
```bash
pip3 install -r requirements.txt
```

3. Run migrations:
```bash
python3 manage.py migrate
```

4. Load sample data:
```bash
python3 manage.py load_properties
python3 manage.py load_investments
```

5. Create a superuser (optional):
```bash
python3 manage.py createsuperuser
```

6. Start the development server:
```bash
python3 manage.py runserver
```

The backend will be available at `http://127.0.0.1:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd front
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 🔑 Key Features

### Property Management
- Dynamic property listings from database
- Property filtering by status (For Sale/For Rent)
- Image gallery with multiple images per property
- Detailed property information (beds, baths, sqft, amenities)
- Interactive property cards and modals

### Investment Opportunities
- Investment opportunity listings
- Investor management
- Investment tracking
- ROI calculations

### Admin Panel
- Modern Django Unfold admin interface
- Property and investment management
- Image upload capabilities
- User and permission management

### Cloud Storage
- DigitalOcean Spaces integration
- CDN delivery for fast image loading
- Automatic file uploads
- Scalable storage solution

## 📚 Documentation

- [Properties Dynamic Loading Guide](back/PROPERTIES_DYNAMIC_LOADING.md)
- [DigitalOcean Spaces Setup](back/DIGITALOCEAN_SPACES_SETUP.md)
- [Investment Feature Guide](back/INVESTMENT_FEATURE.md)
- [Image Upload Guide](back/IMAGE_UPLOAD_GUIDE.md)

## 🔧 Configuration

### Environment Variables (Production)

For production, move sensitive credentials to environment variables:

```bash
# Django
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com

# DigitalOcean Spaces
DO_SPACES_KEY=your-spaces-key
DO_SPACES_SECRET=your-spaces-secret
DO_SPACES_BUCKET_NAME=your-bucket-name
```

### CORS Settings

Update `back/backend/settings.py` to include your production domain:

```python
CORS_ALLOWED_ORIGINS = [
    "https://your-domain.com",
]
```

## 🌐 API Endpoints

### Properties
- `GET /api/properties/` - List all properties
- `GET /api/properties/{id}/` - Get property details
- `GET /api/properties/by_status/?status={status}` - Filter by status
- `POST /api/properties/{id}/upload_image/` - Upload property image

### Investments
- `GET /api/investment-opportunities/` - List all opportunities
- `GET /api/investment-opportunities/{id}/` - Get opportunity details
- `POST /api/investments/` - Create new investment

## 🎨 Design

The platform features a luxury design with:
- Dark theme (#050a14 background)
- Gold accents (#d4af37)
- Serif typography for elegance
- Smooth animations and transitions
- Responsive layout for all devices

## 📞 Contact

**BELLEROCK Holdings Limited**
- Address: 21 Sowutuom, Evans Kwao Street, Accra, Ghana
- Post Address: GC-088-3111
- Email: concierge@bellerock.com

## 📄 License

© 2024 Bellerock Holdings Limited. All Rights Reserved.
