from django.shortcuts import render, redirect, HttpResponse
from .models import Books, Authors

# Create your views here.


def index(request):
    context = {
        'all_books': Books.objects.all()
    }
    return render(request, "many_to_many/index.html", context)


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        Books.objects.create(title=title, description=description)
    return redirect("/")


def book_info(request, book_id):
    this_book = Books.objects.get(id=book_id)
    context = {
        'book': Books.objects.get(id=int(book_id)),
        'all_authors': this_book.authors.all(),
        'all_other_authors': Authors.objects.exclude(books=this_book)
    }

    return render(request, "many_to_many/book_info.html", context)


def link_author(request, book_id):
    print(request.POST, "+*********")
    if request.method == 'POST':
        this_author = Authors.objects.get(id=request.POST['selected_author'])
        this_book = Books.objects.get(id=book_id)
        this_book.authors.add(this_author)

    return redirect(f"/book_info/{book_id}")
