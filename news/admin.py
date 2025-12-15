from django.contrib import admin
from .models import Category, NewsSource, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']


@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'category', 'is_active', 'last_fetched', 'created_at']
    list_filter = ['is_active', 'category', 'country', 'language']
    search_fields = ['name', 'description', 'url']
    readonly_fields = ['last_fetched', 'created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'url', 'rss_url', 'description')
        }),
        ('Classification', {
            'fields': ('category', 'country', 'language')
        }),
        ('Settings', {
            'fields': ('is_active', 'fetch_interval')
        }),
        ('Metadata', {
            'fields': ('last_fetched', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'author', 'published_at', 'fetched_at']
    list_filter = ['source', 'published_at', 'fetched_at', 'categories']
    search_fields = ['title', 'description', 'content', 'author']
    readonly_fields = ['fetched_at']
    date_hierarchy = 'published_at'
    filter_horizontal = ['categories']
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'url', 'source', 'author')
        }),
        ('Content', {
            'fields': ('description', 'content', 'image_url')
        }),
        ('Classification', {
            'fields': ('categories',)
        }),
        ('Metadata', {
            'fields': ('published_at', 'fetched_at'),
        }),
    )
