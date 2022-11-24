from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serialization import BookSerialization


@api_view(['GET', 'GET'])
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerialization(queryset, many=True)
    return Response("Hello API")
