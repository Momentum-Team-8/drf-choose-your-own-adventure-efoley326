from library.models import User, Book, Library
from rest_framework import serializers




class BookSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=200)
    title = serializers.ForeignKey("Library", related_name="book")
    genre = serializers.CharField(max_length=250)
    featured = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Book.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.featured = validated_data.get('featured', instance.featured)
        instance.save()
        return instance

class LibrarySerializer(serializers.Serializer):
    book_profile = serializers.ForeignKey(Book, related_name="books")

    def create(self, validated_data):
        return Library.objects.create(validated_data)

