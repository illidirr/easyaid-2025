from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import TestResult, UserProfile, Video

def index(request):
    return render(request, 'main/index.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                UserProfile.objects.get_or_create(user=user)
                return redirect('profile')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_results = TestResult.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, 'main/profile.html', {
        'user_results': user_results,
        'user_profile': user_profile
    })


def group1(request):
    return render(request, 'main/group1.html')


def group2(request):
    return render(request, 'main/group2.html')


def page1(request):
    videos = Video.objects.filter(page='page1')
    return render(request, 'main/page1.html', {
        'videos': videos,
        'title': 'Страница 1'
    })


def page2(request):
    videos = Video.objects.filter(page='page2')
    return render(request, 'main/page2.html', {
        'videos': videos,
        'title': 'Страница 2'
    })
def page3(request):
    return render(request, 'main/page3.html')


def page4(request):
    return render(request, 'main/page4.html')


def internet_fraud(request):
    videos = Video.objects.filter(page='internet_fraud')
    context = {
        'title': 'Интернет-мошенничество',
        'content': '''
        <p>Интернет-мошенничество — это масштабная и постоянно развивающаяся угроза.</p>
        <p>Злоумышленники ежедневно придумывают новые уловки, но большинство из них основано на старых, проверенных схемах. Знание этих схем — ваша лучшая защита.</p>
        ''',
        'videos': videos
    }
    return render(request, 'main/internet_fraud.html', context)


@login_required
def test(request):
    if request.method == 'POST':
        # Правильные ответы для первого теста (12 вопросов)
        correct_answers = {
            'q1': 'а', 'q2': 'г', 'q3': 'в', 'q4': 'в', 'q5': 'б',
            'q6': 'в', 'q7': 'а', 'q8': 'б', 'q9': 'в', 'q10': 'г',
            'q11': 'а', 'q12': 'в'
        }

        score = 0
        total = len(correct_answers)
        user_answers = {}

        # Проверяем ответы пользователя
        for question, correct_answer in correct_answers.items():
            user_answer = request.POST.get(question)
            user_answers[question] = user_answer
            if user_answer == correct_answer:
                score += 1

        # Сохраняем результат
        TestResult.objects.create(
            user=request.user,
            test_name='Тест: Насколько вы защищены от мошенников?',
            score=score,
            max_score=total,
            answers=user_answers
        )

        # Обновляем профиль
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.tests_completed += 1
        profile.save()

        # Определяем уровень результата
        percentage = int((score / total) * 100)
        if score >= 9:
            level = "Отлично!"
            message = "Вы хорошо защищены от мошенников!"
        elif score >= 5:
            level = "Хорошо"
            message = "Вы в целом защищены, но есть что улучшить."
        elif score >= 2:
            level = "Осторожно!"
            message = "Вы уязвимы для мошенников. Изучите материалы еще раз."
        else:
            level = "Тревога!"
            message = "Вы в высокой группе риска! Срочно изучите материалы."

        return render(request, 'main/test_result.html', {
            'score': score,
            'total': total,
            'percentage': percentage,
            'level': level,
            'message': message,
            'title': 'Результаты теста'
        })

    # Если GET запрос, просто показываем форму теста
    return render(request, 'main/test.html')


@login_required
def test_internet(request):
    if request.method == 'POST':
        # Правильные ответы для теста по интернет-безопасности (10 вопросов)
        correct_answers = {
            'q1': 'в', 'q2': 'б', 'q3': 'а', 'q4': 'г', 'q5': 'в',
            'q6': 'а', 'q7': 'б', 'q8': 'в', 'q9': 'г', 'q10': 'а'
        }

        score = 0
        total = len(correct_answers)
        user_answers = {}

        # Проверяем ответы пользователя
        for question, correct_answer in correct_answers.items():
            user_answer = request.POST.get(question)
            user_answers[question] = user_answer
            if user_answer == correct_answer:
                score += 1

        # Сохраняем результат
        TestResult.objects.create(
            user=request.user,
            test_name='Тест по безопасному пользованию интернетом',
            score=score,
            max_score=total,
            answers=user_answers
        )

        # Обновляем профиль
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.tests_completed += 1
        profile.save()

        # Определяем уровень результата
        percentage = int((score / total) * 100)
        if score >= 8:
            level = "Отлично!"
            message = "Вы отлично разбираетесь в интернет-безопасности!"
        elif score >= 6:
            level = "Хорошо"
            message = "Вы в целом безопасно пользуетесь интернетом."
        elif score >= 4:
            level = "Осторожно!"
            message = "Вам нужно улучшить знания о безопасности в интернете."
        else:
            level = "Тревога!"
            message = "Вы подвергаете себя риску в интернете!"

        return render(request, 'main/test_internet_result.html', {
            'score': score,
            'total': total,
            'percentage': percentage,
            'level': level,
            'message': message,
            'title': 'Результаты теста'
        })

    # Если GET запрос, просто показываем форму теста
    return render(request, 'main/test_internet.html')

def health_check(request):
    """Простой health check для Railway"""
    return HttpResponse("OK", status=200)

def simple_test(request):
    return HttpResponse("Django is working!", status=200)