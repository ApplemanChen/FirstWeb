from django.contrib import admin
from Blog.models import Blog,Category,Tag

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = ["title","click_nums","create_time","modify_time"]

	# 保存数据
	def save_model(self,request,obj,form,change):
		obj.save()
		# 博客分类数目统计
		obj_caterory = obj.category
		category_num = obj_caterory.blog_set.count()
		obj_caterory.number = category_num
		obj_caterory.save()
		# 博客标签数目统计
		obj_tag_list = obj.tag.all()
		for obj_tag in obj_tag_list:
			tag_num = obj_tag.blog_set.count()
			obj_tag.number = tag_num
			obj_tag.save()

	# 删除数据
	def save_model(self,request,obj,form,change):
		obj.save()
		# 博客分类数目统计
		obj_caterory = obj.category
		category_num = obj_caterory.blog_set.count()
		obj_caterory.number = category_num
		obj_caterory.save()
		# 博客标签数目统计
		obj_tag_list = obj.tag.all()
		for obj_tag in obj_tag_list:
			tag_num = obj_tag.blog_set.count()
			obj_tag.number = tag_num
			obj_tag.save()

		

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)