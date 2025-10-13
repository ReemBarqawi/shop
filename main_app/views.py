from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product, Category
from .forms import CategoryForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل الدخول مباشرة بعد التسجيل
            return redirect('product_list')  # أو أي صفحة تحبي توجهي المستخدم بعدها
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
    
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)




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

#--1--product CRUD
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


#--2-- category CRUD

class CategoryListView(ListView):
    model = Category
    template_name = 'main_app/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'main_app/category_detail.html'


class CategoryCreateView(LoginRequiredMixin, IsStaffMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'main_app/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(LoginRequiredMixin, IsStaffMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'main_app/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(LoginRequiredMixin, IsStaffMixin, DeleteView):
    model = Category
    template_name = 'main_app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

