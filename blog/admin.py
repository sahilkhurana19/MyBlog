from django.contrib import admin

# Register your models here.

from .models import Post, Tag

class TagInline(admin.TabularInline):
    model = Tag
    extra = 3

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'was_published_recently')
    fieldsets = [
        (None,  {'fields': ['title']}),
        ('Post Content', {'fields':['desc_sh', 'desc_lg']}),
        ('Date Information', {'fields':['create_date', 'published_date']}),
        ('Miscellaneous', {'fields': ['read_time']})
    ]
    inlines = [TagInline]
    list_filter = ['published_date']


admin.site.register(Post, PostAdmin)
