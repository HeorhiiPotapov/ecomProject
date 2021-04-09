from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class SocialLinks(models.Model):
    name = models.CharField("Название", max_length=30)
    image = models.ImageField("Лого", upload_to="info/social")
    url = models.URLField("Ссылка на профиль")
    is_active = models.BooleanField("Статус", default=True)

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.name


class ProjectRule(models.Model):
    text = models.TextField("Правило")
    is_active = models.BooleanField("Статус", default=True)

    class Meta:
        verbose_name = "Правило проекта"
        verbose_name_plural = "Правила проекта"

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    text = models.TextField("Текс")
    is_active = models.BooleanField("Статус", default=True)

    class Meta:
        verbose_name = "Описание проекта"
        verbose_name_plural = "Описание проекта"

    def __str__(self):
        return self.name


class ProjectFeedback(models.Model):
    sender = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='feedbacks',
                               verbose_name="Пользователь")
    text = models.TextField("Текст")
    timestamp = models.DateTimeField("Время", default=timezone.now)

    class Meta:
        verbose_name = "Отзыв о проекте"
        verbose_name_plural = "Отзывы о проекте"
