from django.contrib import admin
from .models import Book, Genre, BookInstance, Author, Language

# Register your models here.

# admin.site.register(Book)  # Commented out so we can customize the Admin view for this Model
admin.site.register(Genre)
# admin.site.register(BookInstance) # Commented out so we can customize the Admin view for this Model
# admin.site.register(Author) # Commented out so we can customize the Admin view for this Model
admin.site.register(Language)

class BookInline(admin.TabularInline):
    """
    Puts book form information and information about the specific copies (i.e. instances) on the same Book detail form page
    """
    model = Book
    # 'extra' adds the option to add another instance of book with a plus icon
    extra = 0

# to change how a model is displayed in the admin interface, define a ModelAdmin class
@admin.register(Author)  # @admin.register is the same as admin.site.register
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    list_filter = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


class BookInstanceInline(admin.TabularInline):
    """
    Puts book information and information about the specific copies (i.e. instances) on the same Book detail form page
    """
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('author', 'genre')
    fields = [('title', 'author'), ('summary', 'genre'), 'language', 'isbn']
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Basic Info', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )