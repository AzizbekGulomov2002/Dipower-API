from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_9m2r3d4r&u+^e-0#b)5jyq-xtsy*#rxyz9_%=_b2o56*u^lqi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
import os
ALLOWED_HOSTS = ["*"]

X_FRAME_OPTIONS = 'SAMEORIGIN'

AUTHENTICATION_BACKENDS = [
    'apps.users.views.CustomAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "https://api.dipower.ae",
    "https://dipower.ae",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'accept',
    'origin',
    'x-csrftoken',
    'x-requested-with',
    'x-csrf-token',
    'x-xsrf-token'
]
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.landing',
    'apps.orders',
    'apps.users',

    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'config.urls'
AUTH_USER_MODEL = 'users.User'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'DEFAULT_PAGINATION_CLASS': 'apps.app.pagination.BasePagination',
    # 'PAGE_SIZE': 10,

}


JAZZMIN_SETTINGS = {
    "site_title": "Admin Dashboard",
    "site_header": "Dipower Admin",
    "welcome_sign": "Welcome to the Dipower Admin",
    "site_logo": "images/logo.png",  # Add path to your logo
    "login_logo": None,
    "login_logo_dark": None,
    "site_icon": None,
    "user_avatar": None,

    # List of apps to display on the sidebar
    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        # Users app
        "users.User": "fas fa-user",  # Font Awesome icons for User model
        "users.UserProfile": "fas fa-id-card",

        # Orders app
        "orders.Order": "fas fa-box",
        "orders.OrderHistory": "fas fa-history",

        # Landing app (for AboutUs, Statistics, etc.)
        "landing.AboutUs": "fas fa-info-circle",
        "landing.Statistics": "fas fa-chart-bar",
        "landing.CallToUs": "fas fa-phone",
        "landing.Team": "fas fa-users",
        "landing.NewArrival": "fas fa-boxes",

        # Icons for the 'orders' app
        "orders.Category": "fas fa-th",  # Icon for Category model
        "orders.Product": "fas fa-cube",  # Icon for Product model
        "orders.SKU": "fas fa-tag",  # Icon for SKU model
        "orders.ProductImages": "fas fa-images",  # Icon for ProductImages model

        # Add icons for any other models here...
    },

    # UI customizations
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "users"},
        {"app": "orders"},
        {"app": "landing"},
    ],

    "custom_css": None,  # Path to custom CSS if needed
    "custom_js": None,  # Path to custom JS if needed

    # Django admin sidebar and top menu link settings
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "navigation_expanded": True,
    "order_with_respect_to": ["users", "orders", "landing"],  # Order of apps

}



STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
CORS_ALLOW_ALL_ORIGINS = True

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
