from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author

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
    paginate_by = 5
    book_list = 'my_book_list'  # your own name for the list as a template variable
    queryset = Book.objects.all()  # Get all books
    template_name = '../templates/catalog/book_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book
    template_name = '../templates/catalog/book_detail.html'  # Specify your own template name/location


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5
    author_list = 'my_author_list'
    queryset = Author.objects.all()
    template_name = '../templates/catalog/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    # queryset = Book.objects.filter(author='king')
    template_name = '../templates/catalog/author_detail.html'