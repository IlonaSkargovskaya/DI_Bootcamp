from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('add-film/', views.AddFilm.as_view(), name='add_film'),
    path('add-director/', views.AddDirector.as_view(), name='add_director'),
    path('add-review/', views.ReviewCreateView.as_view(), name='add_review'),
    path('edit-film/<pk>', views.EditFilmView.as_view(), name='edit_film'),
    path('edit-director/<pk>', views.EditDirectorView.as_view(), name='edit_director'),
    path('delete-film/<pk>', views.FilmDeleteView.as_view(), name='film_delete'),
    path('favorite-film/<int:film_id>', views.FavouriteFilmView.as_view(), name='favorite_film'),
    path('add-poster/', views.AddPosterView.as_view(), name='add_poster'),
    path('film-detail/<pk>', views.FilmDetailView.as_view(), name='film_detail'),
    path('categories/<int:cat_id>', views.CategoryView.as_view(), name='categories'),
    path('reviews/<int:film_id>', views.film_reviews, name='film_reviews'),
]