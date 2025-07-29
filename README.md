# Bon Voyage

Bon Voyage is a Django-based web application designed to inspire and assist travelers in planning their journeys across the globe. With a focus on user experience, the platform offers curated travel suggestions, mood-based exploration, and AI-powered itinerary generation.

## 🌍 Introduction
Bon Voyage helps users discover destinations, explore by travel mood (Thrill, Cultural, Nature, Romantic), and generate personalized itineraries using generative AI. The project is built with Django and features a modern, responsive UI.

## ✨ Features
- User registration and login
- Explore destinations by mood or country
- AI-powered itinerary generator (using Google Gemini API)
- Beautiful, responsive design with custom CSS
- Contact and About Us pages

## 🗂️ Project Structure
```
BONVOYAGE/
├── BONVOYAGE/           # Django project settings
│   ├── BONVOYAGE/       # Core project config
│   └── accounts/        # Main app: views, templates, static
│       ├── Templates/   # HTML templates
│       ├── static/      # CSS, images, videos
│       ├── forms.py     # Custom forms
│       ├── views.py     # Main views (login, register, itinerary, etc.)
│       ├── urls.py      # App routes
│       └── ...
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
└── venv/                # (optional) Python virtual environment
```

## ⚙️ Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd BonVoyage/BONVOYAGE
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install django google-generativeai
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the app:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 🚀 Usage
- **Register** for a new account or **login** if you already have one.
- Explore destinations by mood (Thrill, Cultural, Nature, Romantic) or by country.
- Use the AI-powered itinerary generator to create a custom travel plan:
  - Enter your destination and number of days.
  - Receive a detailed, day-wise itinerary.
- Visit the About Us and Contact Us pages for more information or to get in touch.

## 🧩 Dependencies
- Django >= 5.1
- google-generativeai

## 📁 Static & Media
- All static files (CSS, images, videos) are located in `accounts/static/accounts/`.
- Templates are in `accounts/Templates/`.

## 👥 Team
- HEER PANCHAL
- JHALAK DEDHIA
- KINJAL PANCHAL

## 📬 Contact
For questions, feedback, or support, please use the Contact Us page in the app.

---
*Bon Voyage – Journey Beyond Boundaries* 
