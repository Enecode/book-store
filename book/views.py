from django.shortcuts import render, get_object_or_404
from .models import Publisher


# Create your views here.
def index(request):
    queryset = Publisher.objects.all()
    return render(request, 'book/index.html', context={"publishers": list(queryset)})


def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, "book/publisher_detail.html", context={"publisher": publisher})
