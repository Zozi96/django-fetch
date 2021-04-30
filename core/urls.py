
from django.contrib import admin
from django.urls import path

from fc.views import FootballClubCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', FootballClubCreateView.as_view())
]
