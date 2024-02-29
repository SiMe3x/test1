from django.contrib import admin
from .models import Product, User_have_product, Lesson, Groupe_product, User_have_groupe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('author','product_name', 'start_product_date')

    def get_changeform_initial_data(self, request):
    	print(request.user.id)
    	return {
        'author': request.user.id,
    	}

@admin.register(Lesson)        
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_name',)

@admin.register(User_have_product)        
class User_have_productAdmin(admin.ModelAdmin):
    list_display = ('student','product')

@admin.register(Groupe_product)        
class Groupe_productAdmin(admin.ModelAdmin):
    list_display = ('groupe_name',)

@admin.register(User_have_groupe)        
class User_have_groupeAdmin(admin.ModelAdmin):
    list_display = ('student','groupe_name',)