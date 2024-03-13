from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from django.urls import reverse


authors_and_books = {
    "William Shakespeare": ["Romeo and Juliet", "Hamlet", "Macbeth"],
    "Jane Austen": ["Pride and Prejudice", "Sense and Sensibility", "Emma"],
    "George Orwell": ["1984", "Animal Farm"],
    "F. Scott Fitzgerald": ["The Great Gatsby", "Tender Is the Night"],
    "Mark Twain": [
        "The Adventures of Huckleberry Finn",
        "The Adventures of Tom Sawyer",
    ],
    "Agatha Christie": ["Murder on the Orient Express", "And Then There Were None"],
    "Leo Tolstoy": ["War and Peace", "Anna Karenina"],
    "Charles Dickens": ["A Tale of Two Cities", "Great Expectations", "Oliver Twist"],
    "Virginia Woolf": ["Mrs. Dalloway", "To the Lighthouse", "Orlando"],
    "Harper Lee": [],
    "Ernest Hemingway": ["The Old Man and the Sea", "A Farewell to Arms"],
    "Fyodor Dostoevsky": ["Crime and Punishment", "The Brothers Karamazov"],
    "Emily Bronte": ["Wuthering Heights"],
    "Franz Kafka": [],
}


def index(request):
    author_list = list(authors_and_books.keys())
    print(author_list)
    return render(request, "authors/index.html", {"authors": author_list})


def author_name_by_number(request, author: int):
    if author >= 1 and author <= 14:
        author_name = list(authors_and_books.keys())[author - 1]
        return HttpResponseRedirect(reverse("author_name", args=[author_name]))
    return HttpResponse("<h1>No author with this name exists</h1>")


# def author_books(request, author: str):
#     print(f"Author = {author}")
#     if author == "williamshakespeare":
#         return HttpResponse("Romeo and Juliet")
#     elif author == "Agatha Christie":
#         return HttpResponse("Murder on the Orient Express")

#     return HttpResponse("Author not found")


def author_books(request, author):
    try:
        return render(
            request,
            "authors/author.html",
            {"author_name": author, "author_books": authors_and_books[author]},
        )
    except:
        # return HttpResponse("<h1>No author found </h1>")
        raise Http404()
