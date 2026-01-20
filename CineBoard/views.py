from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie
from .forms import MovieForm

class MovieListView(ListView):
    model = Movie
    template_name = 'CineBoard/movie_list.html'
    context_object_name = 'movies'

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'CineBoard/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

def movie_search(request):
    query = request.GET.get('q', '')
    genre = request.GET.get('genre', '')
    movies = Movie.objects.all()
    if query:
        movies = movies.filter(title__icontains=query)
    if genre:
        movies = movies.filter(genre=genre)
    return MovieListView.as_view(queryset=movies)(request)
