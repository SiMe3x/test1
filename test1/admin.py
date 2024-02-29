from django.contrib import admin
from .models import Product, Lesson, User_have_product, Groupe_product


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
class LessonAdmin(admin.ModelAdmin):
    list_display = ('Student',)

@admin.register(Groupe_product)        
class LessonAdmin(admin.ModelAdmin):
    list_display = ('groupe_name',)