from django.db import models

# Create your models here.

class User(models.Model):
    GENDER_CHOICES = [
        (1, 'М'),
        (2, 'Ж'),
        (3, '')
    ]
    name = models.CharField(verbose_name='Имя', max_length=150)
    age = models.IntegerField(verbose_name='Возраст')
    gender = models.IntegerField(verbose_name='Пол', choices=GENDER_CHOICES, default=GENDER_CHOICES[2])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['name',]

    def __str__(self) -> str:
        return f'{self.name}'