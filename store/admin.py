from django.contrib import admin
from .models import Category, Writer, Book, Review, Slider


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'create_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('create_at', 'updated_at')


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'create_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('create_at', 'updated_at')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'writer', 'category', 'price', 'stock', 'created', 'updated', 'status')
    search_fields = ('name', 'slug', 'writer__name', 'category__name')
    list_filter = ('category', 'writer', 'status')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created', 'updated')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'review_star', 'created')
    search_fields = ('customer__username', 'book__name')
    list_filter = ('review_star', 'created')
    readonly_fields = ('created',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)
    readonly_fields = ('created', 'updated')
