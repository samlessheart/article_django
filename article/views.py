from django.db.models import query
from django.http.request import QueryDict
import article
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment, Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.urls import reverse

# Create your views here.

def postsearchview(request):
	print(request.GET)
	query_dict= request.GET
	query = query_dict.get('query')
	object_search= None
	if query is not None:
		object_search = Post.objects.filter(title__icontains=query)
	context= {'object_list': object_search}
	return render(request, "article/search.html", context=context)
	

class PostListView(ListView):
	model = Post
	template_name = 'article/home.html'
	context_object_name = 'posts'
	ordering = ['date']
	paginate_by = 4

class PostDetailView(DetailView, FormMixin):
	model = Post
	form_class = CommentForm


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comments'] = Comment.objects.filter(post= self.object,  ).order_by('-date_posted')
		
		return context
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()		
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		form.instance.post = self.object
		form.save()
		return super(PostDetailView, self).form_valid(form)
	
	def get_success_url(self):
		return reverse('article-Detail', kwargs={'pk': self.object.id})
	
            



def about(request):
	return render(request, 'article/about.html') 
	

def contact(request):
	return render(request, 'article/contact.html') 

