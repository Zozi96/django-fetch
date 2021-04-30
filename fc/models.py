from django.db import models


class FootballClub(models.Model):
    name = models.CharField(
        verbose_name='Nombre del club',
        max_length=50,
    )
    foundation_year = models.PositiveIntegerField(
        verbose_name='Año de fundación',
    )
    owner = models.CharField(
        verbose_name='Dueño',
        max_length=50,
    )
    city = models.CharField(
        verbose_name='Ciudad',
        max_length=50,
    )

    class Meta:
        app_label = 'fc'
        db_table = 'futbolclub'
        verbose_name = 'Club de futbol'
        verbose_name_plural = 'Clubs de futbol'

    def __str__(self):
        return self.name
