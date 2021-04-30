from django.contrib import admin
from .models import FootballClub


@admin.register(FootballClub)
class FootballClubAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'foundation_year',
        'owner',
        'city',
    )
    ordering = ('name',)
