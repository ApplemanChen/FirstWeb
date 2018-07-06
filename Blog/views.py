from django.shortcuts import render
from django.views import View
from Blog.models import Blog,Category,Tag

# Create your views here.
class IndexView(View):
	"""首页"""
	def get(self,request):
		all_blog = Blog.objects.all().order_by("-id")
		return render(request,'index.html',{'all_blog':all_blog})

class BlogView(View):
	"""Blog"""
	def get(self,request):
		all_blog = Blog.objects.all().order_by("-id")
		cities = [
		    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
		    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
		    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
		    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
		    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
		    {'name': 'Tokyo2', 'population': '33,000,000', 'country': 'Japan'},
		    {'name': 'Tokyo3', 'population': '33,000,000', 'country': 'Japan'},
		]

		return render(request,'blog.html',{'all_blog':all_blog,'cities':cities})
		