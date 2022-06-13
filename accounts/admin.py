from django.contrib import admin

# Register your models here.
from accounts.models import User, Patient, Doctor, Category, Blog

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Category)
admin.site.register(Blog)



