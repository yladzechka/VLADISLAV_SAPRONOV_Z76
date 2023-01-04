from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name="api-users"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="api-user"),
    path('posts/', views.PostList.as_view(), name="api-posts"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="api-post"),
    path('authors/', views.AuthorList.as_view(), name="api-authors"),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name="api-author"),
    path('books/', views.BookDetail.as_view(), name="api-books"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="api-book"),
]