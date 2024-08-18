from django.db import models


class Country(models.Model):
	name = models.CharField(max_length=100)


class User(models.Model):
	full_name = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="population")


class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="authors")
	experience = models.PositiveIntegerField()
	rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])


class Book(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
	name = models.TextField()
	description = models.TextField()
	rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])


class Review(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
