from django.contrib import admin
from .models import MockTest, Question, Subject, TestResult, UserAnswer

# Register your models here
admin.site.register(MockTest)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(TestResult)
admin.site.register(UserAnswer)
