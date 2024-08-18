from django.contrib import admin
from .models import Country, User, Author, Book, Review


admin.site.register(Country)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
