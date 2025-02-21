from django.db import models
from django.contrib.auth.models import User

# Model to represent a Subject
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Model to represent a Mock Test
class MockTest(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='mock_tests')
    description = models.TextField()
    duration_minutes = models.IntegerField()  # Duration of the test in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Model to represent a Question
# mocktest/models.py

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)  # Renamed field
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    mock_test = models.ForeignKey('MockTest', on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question_text


# Model to represent the test result for a user
class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to User model
    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.user.username} in {self.mock_test.name}"

# Model to store the user's selected answer for each question
class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to User model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1, choices=[('A', 'Option 1'), ('B', 'Option 2'), ('C', 'Option 3'), ('D', 'Option 4')])

    def __str__(self):
        return f"Answer for {self.user.username} in {self.question.mock_test.name} - Q{self.question.id}"
