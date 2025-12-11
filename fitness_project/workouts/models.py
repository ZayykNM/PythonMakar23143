from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Категории тренировок
CATEGORY_CHOICES = [
    ('cardio', 'Кардио'),
    ('strength', 'Силовая'),
    ('yoga', 'Йога/Растяжка'),
]

class Workout(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    category = models.CharField("Категория", max_length=20, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Настройки предпочтений
    want_cardio = models.BooleanField("Хочу Кардио", default=True)
    want_strength = models.BooleanField("Хочу Силовые", default=True)
    want_yoga = models.BooleanField("Хочу Йогу", default=True)

    def __str__(self):
        return f"Профиль {self.user.username}"

# Автоматическое создание профиля при регистрации пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()