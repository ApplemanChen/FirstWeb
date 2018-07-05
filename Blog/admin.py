from django.contrib import admin
from Blog.models import Blog,Category,Tag

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ["title","click_nums","create_time","modify_time"]
		

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)