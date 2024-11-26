from django.core.management.base import BaseCommand

from moviesapp.omdb_integration import search_and_save


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def add_arguments(self, parser):
        parser.add_argument("search", type=str,  nargs="+")

    def handle(self, *args, **options):
        search = " ".join(options["search"])
        search_and_save(search)

