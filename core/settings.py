"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os                 #(static خودم برای)This line imports the os module, which provides a way to interact with the operating system. It allows you to perform operations like joining file paths, which is essential for ensuring that your code works across different operating systems (Windows, macOS, Linux).

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xh7s3*s*+u+zs8fb-rh_rgbmq-pp5&^uzf#yhg=x2#e^iu0b9t'

# SECURITY WARNING: don't run with debug turned on in production!  #پروداکشن منظور همان دیپلوی کنید بیارید روی سرور و میگه اونموقع دیباگ ترو نباش، دیباگ که ترو باشه برای ما باگ‌ها رو نمایش میده و کارای این مدلی، که خب وقتی که داریم دولوپ انجام می‌دیم اوکیه که باشه اما موقع دیپلویی باید فالس قرارش بدید
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

STATIC_URL = '/static/'  #(کامنت خودم) This setting defines the base URL for serving static files. It typically looks like this. This means that when you access گ/static/گ in your browser, Django will know to look for static files.
#دقیقا این نارجی بالا باید همنام با فایلی باشه که در اپ‌مون ساختیم برای فایل‌های استاتیک تا بتونه پیداش کنه
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] #This setting tells Django where to look for additional static files (Static files include assets like CSS, JavaScript, and images that are used in your web application) outside of the default locations (like app directories). You should add the path to your newly created "static" directory. This configuration allows Django to find static files stored in the "static" folder at the root of your project.
#'BASE_DIR' is typically defined earlier in your 'settings.py' file and represents the base directory of your Django project. 'os.path.join(BASE_DIR, 'static')' constructs a full path to the "static" directory located within your project's base directory. This ensures that the path is correctly formatted for the operating system being used.
#By setting 'STATICFILES_DIRS', you inform Django where to find additional static files beyond the default locations (like each app's "static" directory). In this case, it tells Django to look in the "static" folder at the root of your project for any static assets.
#نیست دیگه و جنگو نمیدونه فایلهای استاتیکی که در این ادیشنال استتیک هست رو چجوری باید بیاد پیدا کنه با کمک دستور بالا بهش آدرس اونم میدیم و این یک لیست هست و چندین آدرس مختلف می‌تونیم بهش بدیم STATIC_URL این دیگه جزو اون  additional_static ممکنه ما یکسری فایل‌های استاتیکی داشته باشیم که به هیچکدوم از اپهای پروژه تون ربطی نداره مثلا شما یک فولدر در روت پروژه تون میسازید به نام 




#Set STATIC_ROOT (for production):
#In a production environment, you will want to collect all static files into a single directory from which they can be served. Set this in your settings.py:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #است deploy ما الان با این کاری نداریم این برای زمان 
#The 'collectstatic' command will gather all static files from your apps and any directories specified in 'STATICFILES_DIRS', placing them into the 'STATIC_ROOT'.
#Run collectstatic Command:
#After configuring the settings, run the following command to collect all static files (in all of your applications) into the specified directory (named 'staticfiles'): #  که توی وب سرورتون می‌دید و ریکویست‌هایی که مربوط به فایل‌های استاتیک‌تون باشه میاد رو وب سرورتون میدونه باید از کجا بره جوابشو بده البته قبلش توی کانفیگ سرورتون باید آدرس لوکیشن این فولدر رو بدین. از همین فولدرهstaticfiles شما آدرس این فولدر 
#bash  (توی محیط مجازی مون میریم و دستور پایین رو وارد میکنیم)
#python manage.py collectstatic   #ساخته میشه و تمام فایل‌های استاتیک پروژه تون توش ریخته میشه دقت کنید که اسم فایل‌های استاتیک‌تون رو یکی نگذارید چون بعدا شاید مشکل پیش بیاد staticfiles با زدن این دستور اون فایل 


#these are part of the Django settings configuration for managing media files:
MEDIA_URL = '/media/'  #This setting defines the base URL for serving media files in your Django application. When you upload files (like images, documents, etc.), they will be accessible via URLs that start with '/media/'. For example, if you upload an image named 'example.jpg', it could be accessed at http://yourdomain.com/media/example.jpg.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    #'MEDIA_ROOT' specifies the filesystem path where uploaded media files will be stored. In this case, it sets the path to a directory named media located in the base directory of your Django project (represented by BASE_DIR).The use of 'os.path.join()' ensures that the path is constructed correctly for the operating system being used (Windows, macOS, Linux).
#Together, these settings allow you to manage user-uploaded files in your Django application effectively. 'MEDIA_URL' provides a way to access these files over the web, while 'MEDIA_ROOT' determines where these files are physically stored on the server.
#ما مثلا توی توی فایل مدلها یکجا داشتیم که میخواستیم عکس پروفایل طرف رو بگیریم ازش
#image = models.ImageField(upload_to='profile_images/')   #خط 112 models.py
# درست میکنه و اونجا پروفایل طرف رو ذخیره میکنه و آدرس اون عکسه رو در دیتابیس ذخیره می‌کنه ما که توی دیتابیس عکس نمیتونیم مستقیما ذخیره کنیم باید آدرس عکس رو ذخیره کنیم profile_images و یک فولدر درست میکنه به اسم مدیا و دوباره توی اون یک فولدر دیگه به اسم BLOG_PROJECT این میاد توی رووت اصلی پروژه مون یعنی profile_images توی دستور بالا گفتیم به کاربر که عکس پروفایلش رو در جایی خاصی به نام
#تا اونجا هم تغییراتی اعمال کنیم urls.py بعد از اینا بلافاصله رفتیم در فایل



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.User'