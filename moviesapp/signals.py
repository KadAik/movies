from django.db.models.signals import post_save
from django.dispatch import receiver
from moviesapp.models import SearchTerm

from moviesapp.tasks import notify_of_new_search_term


@receiver(post_save, sender=SearchTerm, dispatch_uid="search_term_saved")
def search_term_saved(sender, instance, created, **kwargs):
    """ Handle (or listen to )a new search being performed event """
    notify_of_new_search_term.delay(instance.term)
