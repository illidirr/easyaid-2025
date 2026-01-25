from django.db import models
from django.contrib.auth.models import User
import json  # Импортируем модуль json


class Video(models.Model):
    PAGE_CHOICES = [
        ('page1', 'Страница 1'),
        ('page2', 'Страница 2'),
        ('internet_fraud', 'Интернет-мошенничество'),
    ]

    title = models.CharField(max_length=200, verbose_name="Название видео")
    description = models.TextField(blank=True, verbose_name="Описание")
    video_file = models.FileField(upload_to='videos/', verbose_name="Видео файл")
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")

    # ДОБАВЛЯЕМ ПОЛЕ PAGE ВНУТРИ КЛАССА Video
    page = models.CharField(
        max_length=20,
        choices=PAGE_CHOICES,
        default='internet_fraud',
        verbose_name="Страница для отображения"
    )

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    score = models.IntegerField()
    max_score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    answers = models.TextField(default='{}')  # Заменяем JSONField на TextField

    def get_answers(self):
        """Возвращает ответы как словарь Python"""
        return json.loads(self.answers)

    def set_answers(self, data):
        """Сохраняет словарь как JSON строку"""
        self.answers = json.dumps(data)

    def __str__(self):
        return f"{self.user.username} - {self.test_name} - {self.score}/{self.max_score}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    tests_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username