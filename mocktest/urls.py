from django.urls import path
from . import views

app_name = 'mocktest'

urlpatterns = [
    path('', views.home, name='home'),
    path('available-tests/', views.available_mock_tests, name='available_mock_tests'),
    path('test/<int:test_id>/', views.test_detail, name='test_detail'),
    path('test/<int:test_id>/start/', views.start_test, name='start_test'),
    path('test/<int:test_id>/submit/', views.submit_test, name='submit_test'),
    path('test/<int:test_id>/result/', views.test_result, name='test_result'),
    path('test/<int:test_id>/add-question/', views.add_question, name='add_question'),
]