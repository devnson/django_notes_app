from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView
)

urlpatterns = [

    path('', NoteListView.as_view(), name = 'note-home'),
    path("note/<int:pk>/", NoteDetailView.as_view(), name='note-detail'),
    path('note/new/', NoteCreateView.as_view(), name = 'note-create'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),

]