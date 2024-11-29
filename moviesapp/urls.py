from django.urls import path
from moviesapp import views

app_label = "moviesapp"

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search-wait/<uuid:result_uuid>/', views.search_wait, name='search_wait'),
    path('search-results/', views.search_results, name='search_results'),
]