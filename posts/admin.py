from django.contrib import admin
from .models import Post, Comment


class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'is_enable', 'publish_date', 'create_time', 'update_time']
    inlines = [CommentAdminInline]



