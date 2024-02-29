from django.db import models
from django.contrib.auth.models import User


class User_have_product(models.Model):	
	Student = models.ForeignKey(User ,on_delete=models.CASCADE)
	
class Product(models.Model):
	product_name = models.CharField(max_length=150, default="")
	author = models.ForeignKey(User ,on_delete=models.CASCADE)
	start_product_date = models.DateTimeField()	
	have_access = models.ForeignKey(User_have_product, on_delete=models.CASCADE)
	price = models.PositiveIntegerField()
	min_users = models.PositiveIntegerField()
	max_users = models.PositiveIntegerField()

class Lesson(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	lesson_name = models.CharField(max_length=150, default="")
	lesson_link = models.SlugField(max_length=300, unique = True)

class Groupe_product(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	groupe_name = models.CharField(max_length=150, default="")
	grope_users = models.ForeignKey(User ,on_delete=models.CASCADE)

