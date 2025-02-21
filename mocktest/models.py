from django.db import models
from django.contrib.auth.models import User



# Model for Subject (e.g., Math, Science, History)
class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
# Model for a Mock Test
class MockTest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Model for a Question in a Mock Test
class Question(models.Model):
    mock_test = models.ForeignKey(MockTest, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)

    def __str__(self):
        return f"Question {self.id} for {self.mock_test.title}"

# Model to Track the Results of a Test Taken by a User
class TestResult(models.Model):
    user = models.ForeignKey(User, related_name='test_results', on_delete=models.CASCADE)
    mock_test = models.ForeignKey(MockTest, related_name='test_results', on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mock_test.title} - Score: {self.score}"

# Model to Track User's Answers for Each Question in a Test
class UserAnswer(models.Model):
    user = models.ForeignKey(User, related_name='user_answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='user_answers', on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - Q{self.question.id}: {self.selected_option}"
