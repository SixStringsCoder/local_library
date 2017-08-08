from django.conf.urls import url

from .views import index, BookListView, BookDetailView


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^books/$', BookListView.as_view(), name="books"),
    url(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),

]
