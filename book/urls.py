from django.urls import path

from . import views

# app_name = "book"
# urlpatterns = [
#     path('', views.index, name='index'),
#     path("<int:pk>/", views.publisher_details, name="publisher_details"),
#     path('book_list/', views.book_list, name="book_list"),
#     path('book_create/', views.book_create, name='book_create')
# ]
urlpatterns = [
    path("book/", views.book_list, name="book_list")
]