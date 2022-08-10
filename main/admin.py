from django.contrib import admin

from main.models import FoodCategory, Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    fields = (
        'category',
        'is_vegan',
        'is_special',
        'code',
        'internal_code',
        'name_ru',
        'description_ru',
        'description_en',
        'description_ch',
        'cost',
        'is_publish',
        'additional',
    )


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    fields = (
        'name_ru',
        'name_en',
        'name_ch',
        'order_id',
    )
