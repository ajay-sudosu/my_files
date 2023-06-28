from django.contrib import admin
from django.urls import path,include
from app import views as app_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', app_views.Quiz_class.as_view()),
    path('quiz/<int:pk>', app_views.Quiz_class.as_view())
]
