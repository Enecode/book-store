from django.urls import path

from . import views

app_name = "book"
urlpatterns = [
    path('', views.index, name='index'),
    path("<int:pk>/", views.publisher_details, name="publisher_details")
]
