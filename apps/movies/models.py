from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Movie(models.Model):
    class TitleType(models.TextChoices):
        SHORT = "short", _("Short")
        MOVIE = "movie", _("Movie")

    imdb_id = models.CharField(_("IMDB id"), max_length=255, null=True)
    title_type = models.CharField(
        _("Type of the title"), max_length=255, choices=TitleType.choices
    )
    name = models.CharField(_("Name"), max_length=255)
    is_adult = models.BooleanField(_("Is Adult"))
    year = models.DateField(_("Release Date"), null=True)
    genres = ArrayField(models.CharField(max_length=255), verbose_name=_("Genres"))

    def __str__(self):
        return f"M: {self.name}"


class Person(models.Model):
    imdb_id = models.CharField(_("IMDB id"), max_length=255, null=True)
    name = models.CharField(_("Name"), max_length=255)
    birth_year = models.DateField(_("Birth Year"), null=True)
    death_year = models.DateField(_("Death Year"), null=True)

    def __str__(self):
        return f"P: {self.name}"


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    order = models.IntegerField(_("Ordering"))
    category = models.CharField(_("Category"), max_length=255)
    job = models.CharField(_("Job"), max_length=255)
    characters = ArrayField(
        models.CharField(max_length=255), verbose_name=_("Characters"), null=True
    )
