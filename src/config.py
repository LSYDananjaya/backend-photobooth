import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    CORS_ORIGINS = ['https://frontend-photobooth.vercel.app', 'http://localhost:3000', 'http://localhost:5173', 'https://backend-photobooth-production.up.railway.app']


class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
