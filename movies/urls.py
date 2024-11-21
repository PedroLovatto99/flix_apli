from django.urls import path
from .views import *


urlpatterns = [
    path("movies/", MovieCreateListView.as_view(), name='movie-create-list'),
    path("mmovies/<int:pk>/", MovieRetrieverUpdateDestroyView.as_view(), name="movie-detail-view"),
    # path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats-view')
]
