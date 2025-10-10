from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product

# Only allow staff/admin users to access certain views
class IsStaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

        

# Public list/detail pages without login 
class ProductListView(ListView):
    model = Product
    template_name = 'main_app/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main_app/product_detail.html'

#========================================================


# Admin CRUD pages
class ProductCreateView(LoginRequiredMixin, IsStaffMixin, CreateView):
    model = Product
    fields = ['name','description','price','stock','category','image']
    template_name = 'main_app/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(LoginRequiredMixin, IsStaffMixin, UpdateView):
    model = Product
    fields = ['name','description','price','stock','category','image']
    template_name = 'main_app/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(LoginRequiredMixin, IsStaffMixin, DeleteView):
    model = Product
    template_name = 'main_app/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
