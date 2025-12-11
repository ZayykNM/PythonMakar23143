from django.contrib import admin
from django.urls import path, include  # <-- Важно: добавили include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workouts.urls')), # <-- Эта строчка подключает твоё приложение
]