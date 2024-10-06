from django.contrib import admin
from django.urls import path
from notes.views import Notes_view, delete_note, done_or_not_notes
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Notes_view.as_view()),
    path('category/<str:category>/', Notes_view.as_view()),
    path('delete/<int:pk>/', delete_note),
    path('onclick/<int:pk>/', done_or_not_notes),
    path('category/<str:category>/onclick/<int:pk>/', done_or_not_notes),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
