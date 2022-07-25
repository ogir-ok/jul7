import json
import os.path
from django.core.management.base import BaseCommand, CommandError
from apps.movies.models import Movie, Person, PersonMovie
from csv import DictReader, excel_tab


class Command(BaseCommand):

    help = "Imports person+movies from tsv file"

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
                    "ordering",
                    "nconst",
                    "category",
                    "job",
                    "characters",
                ]
            )

            for line in data:

                if not line:
                    continue

                if not line['tconst'].startswith('tt'):
                    continue

                movie_id = Movie.objects.filter(imdb_id=line['tconst']).first()
                if not movie_id:
                    continue

                person_id = Person.objects.filter(imdb_id=line['nconst']).first()
                if not person_id:
                    continue

                person_movie_data = {
                    "order": int(line['ordering']),
                    "category": line['category'],
                    "job": None if line['job'] == "\\N" else line['job'],
                    "characters": None if line['characters'].startswith("\\N") else json.loads(line['characters']),
                }

                PersonMovie.objects.get_or_create(movie_id=movie_id, person_id=person_id, defaults=person_movie_data)
