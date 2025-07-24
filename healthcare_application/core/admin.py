from django.contrib import admin
from .models import Patient, Doctor
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(User)
