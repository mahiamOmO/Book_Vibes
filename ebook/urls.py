from django.urls import path, include
from ebook import views


urlpatterns = [
    path('', views.ebook_view, name='ebook'),
    path('add/', views.add_ebook, name='add_ebook'),
    path('<int:id>/delete/', views.delete_ebook, name='delete_ebook'),
    path('<int:id>/update/', views.update_ebook, name='update_ebook'),
    path('<int:id>/', views.ebook_details, name='ebook_details'),
    path('<int:ebook_id>/read/<int:chapter_id>/', views.read_chapter, name='read_chapter'),
    path('<int:ebook_id>/add-chapter/', views.add_chapter, name='add_chapter'),
]
