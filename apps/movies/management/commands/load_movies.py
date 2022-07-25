import os.path
from django.core.management.base import BaseCommand, CommandError
from apps.movies.models import Movie
from csv import DictReader, excel_tab


class Command(BaseCommand):

    help = "Imports movies from tsv file"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str, required=True)

    def handle(self, *args, **options):
        file = options.get("file")

        if not os.path.exists(file):
            raise CommandError("File does not exist")

        with open(file, encoding="utf-8") as fileopen:

            data = DictReader(
                fileopen,
                dialect=excel_tab,
                fieldnames=[
                    "tconst",
                    "titleType",
                    "primaryTitle",
                    "originalTitle",
                    "isAdult",
                    "startYear",
                    'endYear',
                    'runtimeMinutes',
                    'genres'
                ],
            )

            for line in data:

                if not line:
                    continue

                if not line['tconst'].startswith('tt'):
                    continue

                movie_data = {
                    "title_type": line['titleType'],
                    "name": line['primaryTitle'],
                    "is_adult": line['isAdult'],
                    "date": None if line['startYear'] == "\\N" else f"{line['startYear']}-01-01",
                    "genres": line['genres'].split(","),
                }

                movie, created = Movie.objects.get_or_create(imdb_id=line['tconst'], defaults=movie_data)

                if created:
                    Movie.objects.filter(id=movie.id).update(**movie_data)
