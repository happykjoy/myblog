from django.contrib import admin
from .models import Category,Tag,Tui,Article,Banner,Link

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','excerpt','categary','img','body','views','tui','created_time','modified_time')
    list_per_page = 2
    ordering = ('-created_time',)
    list_display_links = ('id','title')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('text_info','img','link_url','is_active',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','index','id')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','linkurl')