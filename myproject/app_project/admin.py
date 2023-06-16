from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Topic)
admin.site.register(BlogPost)
#admin.site.register(Comment)
admin.site.register(Like)

# Join column in admin panel
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'updated_at')
    
admin.site.register(Comment,CommentAdmin)