from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Products

# Create your views here.

def home(request):
	context = {
        'products': Products.objects.filter(product_vendor = 'A')
    }
	return render(request, 'shopKeeper/index.html', context)

class ProductListView(ListView):
	model = Products
	template_name = 'shopKeeper/index.html'
	context_object_name = 'products'
	def get_queryset(self):
		return Products.objects.filter(product_vendor = self.request.user.id)
	ordering = ['-product_price']


class ProductDetailView(LoginRequiredMixin, DetailView):
	model = Products
	def get_queryset(self):
		return Products.objects.filter(product_vendor = self.request.user.id)

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Products
	fields = [
		'product_name', 
		'product_price', 
		'product_unit', 
		'product_discount', 
		'product_description', 
		'product_stock', 
		'product_image',
	]
	success_url = '/'
	template_name = 'shopKeeper/upload_product.html'

	def form_valid(self, form):
		form.instance.product_vendor = self.request.user
		return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Products
	fields = [
		'product_name', 
		'product_price',
		'product_unit',  
		'product_discount', 
		'product_description', 
		'product_stock',
	]

	def form_valid(self, form):
		form.instance.product_vendor = self.request.user
		return super().form_valid(form)

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.product_vendor:
			return True
		return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Products
	success_url = '/'

	def get_queryset(self):
		return Products.objects.filter(product_vendor = self.request.user.id)

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.product_vendor:
			return True
		return False

