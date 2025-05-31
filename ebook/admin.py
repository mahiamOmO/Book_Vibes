from django.contrib import admin
from .models import Ebook, Chapter

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

class EbookAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]

admin.site.register(Ebook, EbookAdmin)
admin.site.register(Chapter)
