from gh import views
from django.urls import path

app_label = "gh"

urlpatterns = [
    path('', views.index, name='index'),
]