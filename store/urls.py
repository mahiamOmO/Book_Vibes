from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
	path('', views.index, name = "index"),
	path('login', views.signin, name="signin"),
	path('logout', views.signout, name="signout"),
	path('registration', views.registration, name="registration"),
	path('book/<int:id>', views.get_book, name="book"),
	path('book/add/', views.add_new_book, name="add_new_book"),
	path('book/edit/<int:id>/', views.edit_book, name="edit_book"),
	path('book/delete/<int:id>', views.delete_book, name="delete_book"),
	path('books', views.get_books, name="books"),
	path('category/<int:id>', views.get_book_category, name="category"),
	path('writer/<int:id>', views.get_writer, name = "writer"),
	path('product/<int:id>/details/', views.product_details, name = "product_details"),
]
