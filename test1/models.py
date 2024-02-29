from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



	
class Product(models.Model):
	product_name = models.CharField(max_length=150, default="Product")
	author = models.ForeignKey(User ,on_delete=models.CASCADE)
	start_product_date = models.DateTimeField(default = timezone.now)
	#have_access = models.ManyToManyField(User_have_product)
	price = models.PositiveIntegerField(default=1)
	min_users = models.PositiveIntegerField(default=2)
	max_users = models.PositiveIntegerField(default=3)

	def __str__(self):
		return f"{self.product_name}, {self.author},{self.start_product_date}"

class User_have_product(models.Model):	
	student = models.ForeignKey(User ,on_delete=models.CASCADE)
	product = models.ForeignKey(Product ,on_delete=models.CASCADE)
	
	def __str__(self):
		return f"{self.student}, {self.product}"

class Lesson(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	lesson_name = models.CharField(max_length=150, default="")
	lesson_link = models.SlugField(max_length=300, unique = True)
	def __str__(self):
		return f"{self.product}, {self.lesson_name},{self.lesson_link}"


class Groupe_product(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	groupe_name = models.CharField(max_length=150, default="")
	#grope_users = models.ForeignKey(User ,on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.product}, {self.groupe_name}"

class User_have_groupe(models.Model):	
	student = models.ForeignKey(User_have_product ,on_delete=models.CASCADE)
	groupe_name = models.ForeignKey(Groupe_product ,on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.student}, {self.groupe_name}"

