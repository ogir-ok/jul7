import os

from .docker import *


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT =  os.getenv('EMAIL_PORT', '587')
EMAIL_HOST_USER =   os.getenv('EMAIL_HOST_USER', '275924@gmail.com')
EMAIL_HOST_PASSWORD =   os.getenv('EMAIL_HOST_PASSWORD', '123')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'true').lower() in ('1', 'true')


DEBUG = False

ALLOWED_HOSTS = ['3.88.174.111', 'jul7.ogir-ok.com']