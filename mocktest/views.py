from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MockTest, Question

# Home view
def home(request):
    return render(request, 'mocktest/home.html')

# View to show all available mock tests
def available_mock_tests(request):
    mock_tests = MockTest.objects.all()
    return render(request, 'mocktest/available_mock_tests.html', {'mock_tests': mock_tests})

# View to show details of a specific mock test
def test_detail(request, test_id):
    mock_test = get_object_or_404(MockTest, id=test_id)
    return render(request, 'mocktest/test_detail.html', {'mock_test': mock_test})

# View to start a mock test
def start_test(request, test_id):
    mock_test = get_object_or_404(MockTest, id=test_id)
    questions = mock_test.questions.all()  # Assuming a related name for questions in MockTest model
    return render(request, 'mocktest/start_test.html', {'mock_test': mock_test, 'questions': questions})

# View to handle test submission
def submit_test(request, test_id):
    if request.method == 'POST':
        mock_test = get_object_or_404(MockTest, id=test_id)
        questions = mock_test.questions.all()
        selected_answers = {}

        # Process each question's answer
        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            if selected_answer:
                selected_answers[question.id] = selected_answer

        # Save or process the selected answers (e.g., calculate score)
        # For now, just return a simple response
        return HttpResponse(f"Test submitted! Your answers: {selected_answers}")

    return redirect('mocktest:start_test', test_id=test_id)

# View to display test result
def test_result(request, test_id):
    mock_test = get_object_or_404(MockTest, id=test_id)
    # Add logic to calculate and display the result
    return render(request, 'mocktest/test_result.html', {'mock_test': mock_test})

# View to add a question to a mock test
def add_question(request, test_id):
    mock_test = get_object_or_404(MockTest, id=test_id)
    if request.method == 'POST':
        # Process form data to add a new question
        question_text = request.POST.get('question_text')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correct_answer = request.POST.get('correct_answer')

        # Create and save the new question
        question = Question.objects.create(
            mock_test=mock_test,
            question_text=question_text,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_answer=correct_answer
        )
        return redirect('mocktest:test_detail', test_id=test_id)

    return render(request, 'mocktest/add_question.html', {'mock_test': mock_test})