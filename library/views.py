from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'library/list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['-date_add']
    paginate_by = 5


class UserBookListView(ListView):
    model = Book
    template_name = 'library/user.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(owner=user).order_by('-date_add')


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/detail.html'
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'library/book.html'
    fields = ['title', 'author', 'cover', 'file']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'library/book.html'
    fields = ['title', 'author', 'cover', 'file']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.owner:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'library/delete.html'
    success_url = '/'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.owner:
            return True
        return False
