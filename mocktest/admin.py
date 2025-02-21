from django.contrib import admin
from .models import Subject, Question, MockTest, User, UserTestResult

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(MockTest)
admin.site.register(UserTestResult)
# mocktest/admin.py
from django.contrib import admin
from .models import MockTest, UserTestResult  # Import your models

# Register your models
# mocktest/admin.py
from django.contrib import admin
from .models import MockTest, UserTestResult  # Register your models, not User

# Registering your custom models

