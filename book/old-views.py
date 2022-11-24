from django.shortcuts import render, get_object_or_404
from .models import Publisher, Book
from django.db.models import Count, Min, Max, Sum
from .forms import BookForm

# Create your views here.
def index(request):
    queryset = Publisher.objects.all()
    return render(request, 'book/index.html', context={"publishers": list(queryset)})


def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, "book/publisher_detail.html", context={"publisher": publisher})


def book_list(request):
    queryset = Book.objects.select_related('publisher')
    queryset.aggregate(Count('id'))
    return render(request, 'book/book_list.html', context={"books": list(queryset)})


def book_create(request):
    """Creating instance of the form"""
    if request.method == 'GET':
        form = BookForm()
    elif request.method =='POST':
        print(request.POST)
        form = BookForm(request.POST)
        return render(request, "book/book_create.html", context={"form": form})