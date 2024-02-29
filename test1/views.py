from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from .models import Product, User_have_product, Lesson, Groupe_product, User_have_groupe
from django.shortcuts import render

def index(request):
    #print(Product)
    product_list=Product.objects.all()
    students_list=User_have_product.objects.all()
    
    return render(request, 'test1/index.html',{'product_list':product_list,'students_list':students_list})