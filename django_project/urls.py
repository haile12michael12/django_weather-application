
from django.contrib import admin
from django.urls import path
from dictionary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search_word, name='search_word'),
]
