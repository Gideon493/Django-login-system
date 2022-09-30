from atexit import register
from django.contrib import admin

from accounts.models import User

admin.site.register(User)

# Register your models here.
