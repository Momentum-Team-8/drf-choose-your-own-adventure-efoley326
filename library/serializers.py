from .models import User, Book, Library
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'genre', 'featured']
    
    def create(self, validated_data):
        return Book.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.featured = validated_data.get('featured', instance.featured)
        instance.save()
        return instance

class LibrarySerializer(serializers.ModelSerializer):
    model = Library
    fields = [
    'book_profile']

    @classmethod
    def many_init(Library, *args, **kwargs):
        kwargs['Book'] = Library()
        return Library(*args, **kwargs)

    def create(self, validated_data):
        return Library.objects.create(validated_data)
