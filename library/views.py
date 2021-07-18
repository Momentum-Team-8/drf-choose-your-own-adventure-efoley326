from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from library.models import Book, Library
from library.serializers import BookSerializer, LibrarySerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, kwargs):
        content = JSONRenderer().render(data)
        kwargs['book_info'] = 'library/json'
        super(JSONResponse, self).__init__(content, kwargs)

def library(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = LibrarySerializer(books, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibrarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)

def book_info(request,pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)





