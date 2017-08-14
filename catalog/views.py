from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, BookInstance, Author

# Create your views here.

@login_required
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
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'num_books': num_books, 'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'num_authors': num_authors, 'num_genres': num_genres,
               'num_visits': num_visits}
    return render(request, 'index.html', context)


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 5
    book_list = 'my_book_list'  # your own name for the list as a template variable
    queryset = Book.objects.all()  # Get all books
    template_name = '../templates/catalog/book_list.html'  # Specify your own template name/location
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = '../templates/catalog/book_detail.html'  # Specify your own template name/location
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 5
    author_list = 'my_author_list'
    queryset = Author.objects.all()
    template_name = '../templates/catalog/author_list.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    # queryset = Book.objects.filter(author='king')
    template_name = '../templates/catalog/author_detail.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'