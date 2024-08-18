from django.urls import path
from .views import books_view, add_data


urlpatterns = [
	path("books/<str:query_type>", books_view, name="books-list"),
	path("add", add_data, name="seeder"),
]
