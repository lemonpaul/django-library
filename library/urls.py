from django.urls import path
from .views import (
	BookListView,
    UserBookListView,
	BookDetailView,
	BookCreateView,
	BookUpdateView,
	BookDeleteView
)

urlpatterns = [
    path('', BookListView.as_view(), name='library-home'),
    path('user/<str:username>', UserBookListView.as_view(), name='user-books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
