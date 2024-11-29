from django.core.signals import Signal

movie_filled = Signal()

__all__ = ("movie_filled", )