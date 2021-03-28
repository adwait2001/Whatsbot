from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Products(models.Model):
	product_name = models.CharField(max_length=200)
	product_price = models.BigIntegerField()
	product_discount = models.BigIntegerField()
	product_description = models.TextField()
	product_unit = models.CharField(max_length=100)
	product_stock = models.BigIntegerField()
	product_image = models.ImageField(default = 'default.jpg', upload_to = 'product_pics', blank=True, null=True)
	product_vendor = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.product_name

	def get_absolute_url(self):
		return reverse('product-detail', kwargs = {'pk': self.pk})