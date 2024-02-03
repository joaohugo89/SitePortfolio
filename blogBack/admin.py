from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Category

class CommentItemInLine(admin.TabularInline):
    model = Comment
    raw_id_fields = ["post"]

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "intro", "body"]
    list_display = ["title", "slug", "category", "created_at", "status"]
    list_filter = ["category", "created_at", "status"]
    inlines = [CommentItemInLine]
    prepopulated_fields = {"slug":("title",)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]
    prepopulated_fields = {"slug":("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "post", "created_at"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)