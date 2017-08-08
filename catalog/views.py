from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author, Genre

# Create your views here.


def index(request):
    """
    View function for home page of site, index.html.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_genres = Book.objects.all().count()

    context = {'num_books': num_books, 'num_instances': num_instances,
               'num_instances_available': num_instances_available, 'num_authors': num_authors, 'num_genres': num_genres}
    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'  # your own name for the list as a template variable
    queryset = Book.objects.all()  # Get 5 books containing the title war
    template_name = 'catalog/templates/book_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/templates/book_detail.html'  # Specify your own template name/location
