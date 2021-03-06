import sys
import os
from django.conf import settings

BASE_DIR = os.path.dirname(__file__)
settings.configure(
    DEBUG = True,
    SECRET_KEY = '',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    #INSTALLED_APPS = [
        #'django.contrib.staticfiles',
       # 'sitebuilder',
   # ],
    INSTALLED_APPS = [
        #'django.contrib.admin',
        #'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
             'DIRS':[
                 '/home/liunx/PycharmProjects/sitebuilder/sitebuilder/templates'
             ],
            'APP_DIRS':True,
        },
    ),
    STATIC_URL = '/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR,'pages'),
)

if __name__ ==  "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

