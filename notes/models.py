from django.db import models

# Create your models here.

class Notes(models.Model):
    class Category(models.TextChoices):
        WORK = 'Работа'
        FAMILY = 'Семья'
        PERSONAL = 'Личное'
        HOME = 'Дом'
        HEALTH = 'Здоровье'
        MONEY = 'Деньги'

    article = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    category = models.TextField(choices=Category.choices, default='Другое')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.article