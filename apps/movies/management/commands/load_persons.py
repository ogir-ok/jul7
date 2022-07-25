import os.path
from django.core.management.base import BaseCommand, CommandError
from apps.movies.models import Person
from csv import DictReader, excel_tab


class Command(BaseCommand):

    help = "Imports persons from tsv file"

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
                    "nconst",
                    "primaryName",
                    "birthYear",
                    "deathYear",
                    "primaryProfession",
                    "knownForTitles",
                ],
            )

            for line in data:

                if not line:
                    continue

                if not line['nconst'].startswith('nm'):
                    continue

                person_data = {
                    "name": line['primaryName'],
                    "birth_date": None if line['birthYear'] == "\\N" else f"{line['birthYear']}-01-01",
                    "death_date": None if line['deathYear'] == "\\N" else f"{line['deathYear']}-01-01",
                }
                person, created = Person.objects.get_or_create(imdb_id=line['nconst'], defaults=person_data)

                if created:
                    Person.objects.filter(id=person.id).update(**person_data)
