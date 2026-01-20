from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Review


class HomeView(ListView):
    model = Product
    template_name = 'products_app/home.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:5]


class ProductListView(ListView):
    model = Product
    template_name = 'products_app/products_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_app/products_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product=self.object)
        return context


class ReviewCreateView(CreateView):
    model = Review
    fields = ['author_name', 'text', 'rating']
    template_name = 'products_app/add_review.html'

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['product_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'product_id': self.kwargs['product_id']})


class SearchView(ListView):
    model = Product
    template_name = 'products_app/search.html'
    context_object_name = 'products'

    def get_queryset(self):
        q = self.request.GET.get('s')
        return Product.objects.filter(name__icontains=q) if q else Product.objects.all()


class BlogView(TemplateView):
    template_name = 'products_app/blog.html'


class AboutView(TemplateView):
    template_name = 'products_app/about.html'


class BasketView(TemplateView):
    template_name = 'products_app/basket.html'


class HashtagsView(TemplateView):
    template_name = 'products_app/hashtags.html'


class ContactView(TemplateView):
    template_name = 'products_app/contact.html'
