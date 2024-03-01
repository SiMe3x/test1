from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from .models import Product, User_have_product, Lesson, Groupe_product, User_have_groupe
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    #print(Product)
    product_list=Product.objects.all()
    students_list=User_have_product.objects.all()
    print(product_list)
    return render(request, 'test1/index.html',{'product_list':product_list,'students_list':students_list})

def get_acsess(request):
    product_list = Product.objects.all()
    students_list = User.objects.filter(groups__name='Student')
    #print(students_list)
    page_status= 'страница загружена'
    try:
        a = request.POST["student"]
        b = request.POST["product"]
        if User_have_product.objects.filter(student = a, product = b):
            page_status = 'Студент уже записан на курс'
        else:
            User_have_product.objects.get_or_create(student=User.objects.get(id=a), product=Product.objects.get(id=b))
            page_status = str(User_have_product.objects.get(student=User.objects.get(id=a), product=Product.objects.get(id=b)).student) + ' записан на '+ str(User_have_product.objects.get(student=User.objects.get(id=a), product=Product.objects.get(id=b)).product.product_name)


    #print(User_have_product.objects.filter(student=a))

    except:
        print('error')


    return render(request, 'test1/get_acsess.html',{'product_list':product_list,
                                                    'students_list':students_list,
                                                    'page_status':page_status})
