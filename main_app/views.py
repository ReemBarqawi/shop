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


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('product_list') 
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


#========================================================
# Customer pages 

@login_required
def cart_view(request):
    # جلب أو إنشاء order مؤقت للمستخدم
    order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    items = order.items.all()
    return render(request, 'main_app/cart.html', {'order': order, 'items': items})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.stock <= 0:
        return redirect('product_detail', pk=product.id)  # لا يوجد stock

    order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    item.delete()
    return redirect('cart')

@login_required
def checkout_view(request):
    order = get_object_or_404(Order, user=request.user, status='Pending')
    if request.method == 'POST':
        # تحديث stock للمنتجات
        for item in order.items.all():
            item.product.stock -= item.quantity
            item.product.save()
        # تحديث حالة الطلب
        order.status = 'Shipped'  # أو Pending لو بدك يتغير بعد الدفع
        order.save()
        return render(request, 'main_app/checkout_success.html', {'order': order})

    return render(request, 'main_app/checkout.html', {'order': order})