from django.urls import path
from . import views

urlpatterns = [
    # path(
    #     "<str:author>",
    #     views.author_name,
    # ),
    path("", views.index, name="index"),
    path("<int:author>", views.author_name_by_number),
    path("<str:author>", views.author_books, name="author_name"),
]
