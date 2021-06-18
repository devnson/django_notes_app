from typing import List
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Note

# Create your views here.

@login_required(login_url='/login/')


def home(request):

    context = {
        'notes': Note.objects.all()
    }

    return render(request, 'content/home.html', context)


class NoteListView(ListView):
    model = Note
    template_name = 'content/home.html'
    context_object_name = 'notes'
    ordering = ['-date_posted']


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteDetailView(DetailView):
    model = Note
