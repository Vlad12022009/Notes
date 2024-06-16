from django.contrib import admin
from django.urls import path
from notes.views import notes_view, notes_view_all, Create_notes, delete_note, done_or_not_notes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes_view_all),
    path('category/<str:category>/', notes_view),
    path('notes_form/', Create_notes.as_view()),
    path('delete/<int:pk>/', delete_note),
    path('onclick/<int:pk>/', done_or_not_notes),
    path('category/<str:category>/onclick/<int:pk>/', done_or_not_notes),
]
