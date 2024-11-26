from django.core.management import BaseCommand
from moviesapp.models import Movie
import logging
from moviesapp.omdb_integration import fill_movie_details

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def add_arguments(self, parser):
        parser.add_argument("imdb_id", type=str, nargs=1)

    def handle(self, *args, **options):
        try:
            movie = Movie.objects.get(imdb_id=options["imdb_id"][0])
        except Movie.DoesNotExist:
            logger.error("Movie with IMDB ID '%s' was not found", options["imdb_id"][0])
            return

        fill_movie_details(movie)
