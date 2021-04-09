from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Product, Image
from .forms import ProductForm, ImageForm
from .mixins import IsOwnerMixin
from django.http import Http404


class ImagePermissionsMixin:
    def get(self, *args, **kwargs):
        product = self.get_object().product
        if not self.request.user == product.owner:
            raise Http404
        return super().get(*args, **kwargs)


class ProductListView(generic.ListView):
    """
    product list queryset can be a filtered by category
    name, or include all products ordered by creation date
    """
    model = Product
    template_name = 'products/list.html'
    paginate_by = 16

    def get_queryset(self, **kwargs):
        category = None
        qs = super().get_queryset()
        cat_slug = self.kwargs.get('cat_slug')
        if cat_slug:
            """
            use get_descendants() to include all children's
            category products in queryset
            """
            category = get_object_or_404(
                Category,
                slug=cat_slug).get_descendants(include_self=True)
            qs = qs.filter(category__in=category)
        return qs


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:all')

    def form_valid(self, form):
        if form.is_valid():
            p_form = form.save(commit=False)
            p_form.owner = self.request.user
            p_form.save()
            return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin,
                        IsOwnerMixin,
                        generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit.html'

    def get_success_url(self):
        return reverse_lazy('products:detail',
                            args=[self.get_object().pk])


class ProductDeleteView(LoginRequiredMixin,
                        IsOwnerMixin,
                        generic.DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:all')


class ImageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'products/image_create.html'

    def get(self, *args, **kwargs):
        product = Product.objects.get(pk=self.kwargs['pk'])
        if not self.request.user == product.owner:
            raise Http404
        return super().get(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('products:detail',
                            args=[self.kwargs['pk']])

    def form_valid(self, form):
        if form.is_valid:
            new = form.save(commit=False)
            new.product = Product.objects.get(pk=self.kwargs['pk'])
            new.save()
            return super().form_valid(form)


class ImageEditView(LoginRequiredMixin,
                    ImagePermissionsMixin,
                    generic.UpdateView):
    model = Image
    form_class = ImageForm
    template_name = 'products/image_edit.html'

    def form_valid(self, form):
        if form.is_valid():
            new = form.save(commit=False)
            new.product = self.get_object().product
            new.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('products:detail',
                            args=[self.get_object().product.pk])


class ImageDeleteView(LoginRequiredMixin,
                      ImagePermissionsMixin,
                      generic.DeleteView):
    model = Image
    template_name = 'products/image_delete.html'
    success_url = reverse_lazy('products:all')

    def get_success_url(self):
        return reverse_lazy('products:detail',
                            args=[self.get_object().product.pk])
