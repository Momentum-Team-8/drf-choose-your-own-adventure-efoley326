from library.models import Book, Library, User
from library.serializers import BookSerializer, LibrarySerializer, UserSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class TheLibrary(APIView):

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = LibrarySerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookProfile(APIView):

    def get_book(self, pk):
        return Book.objects.get(pk=pk)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




