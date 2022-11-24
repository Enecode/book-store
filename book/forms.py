from django import forms
from .models import  Book


class BookForm(forms.Form):
    title = forms.CharField(max_length=255)
    isbn = forms.CharField(max_length=255)

    class Meta:
        model = Book
        # fields = '__all__'
        # fields = []

