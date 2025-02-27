# mocktest/urls.py
from django.urls import path
from . import views

# Define the app_name here
app_name = 'mocktest'

urlpatterns = [
    path('', views.home, name='home'),
    path('available/', views.available_mock_tests, name='available_mock_tests'),
    path('test/<int:test_id>/', views.test_detail, name='test_detail'),
    path('start_test/<int:test_id>/', views.start_test, name='start_test'),
    path('submit_test/<int:test_id>/', views.submit_test, name='submit_test'),
    path('test_result/<int:test_id>/', views.test_result, name='test_result'),
    path('add_question/<int:test_id>/', views.add_question, name='add_question'),
]
