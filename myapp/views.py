import random
from datetime import datetime

from django.http import HttpResponse
from django.db import connection
from .models import Country, User, Author, Book, Review


def books_view(request, query_type: str):
	now = datetime.now()
	response = ""
	if query_type == "simple":
		# Clear queries list before executing your queries
		connection.queries_log.clear()
		for book in Book.objects.all():
			print("Author:", book.author.user.full_name)
		response = f"Simple queries count: {len(connection.queries)}"
	elif query_type == "select_related":
		# Clear queries list before executing your queries
		connection.queries_log.clear()
		for book in Book.objects.select_related("author__user").all():
			print("Author:", book.author.user.full_name)
		response = f"Select related queries count: {len(connection.queries)}"
	elif query_type == "prefetch_related":
		# Clear queries list before executing your queries
		connection.queries_log.clear()
		for book in Book.objects.prefetch_related('reviews__user').all():
			for review in book.reviews.all():
				print("User:", review.user.full_name)
		response = f"Prefetch related queries: {connection.queries}"
	then = datetime.now()
	difference = (then - now).seconds
	return HttpResponse(response + f"\nDone in {difference}s")


def add_data(request):
	now = datetime.now()
	countries = Country.objects.bulk_create([Country(name=f"Country {i}") for i in range(100)])
	users = User.objects.bulk_create(
		[User(full_name=f"Full name {i}", email=f"email.{i}@gmail.com", country=random.choice(countries)) for i in
		 range(200)])
	authors = Author.objects.bulk_create(
		[Author(user=user, experience=random.randint(1, 10), rating=5) for user in users])
	books = Book.objects.bulk_create(
		[Book(name=f"Book {i}", description=f"Description {i}", author=random.choice(authors), rating=5) for i in
		 range(1000000)]
	)
	Review.objects.bulk_create([Review(book=random.choice(books), user=random.choice(users), content=f"Content {i}") for i in range(1000)])
	then = datetime.now()
	difference = (then - now).seconds
	return HttpResponse(f"Done in {difference}s")
