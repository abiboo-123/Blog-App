from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Post, Contact, Comment, Category
from .forms import contactForm, commentForm
from django.views.generic import ListView
# Create your views here.

def index(request):
    
    posts = Post.mewmanager.all()
    content = {'posts': posts}
    
    return render(request, 'index.html', content)

def redir(request):
    return redirect(index)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})

def postDetails(request, pk):
    post = Post.objects.get(id=pk, status='published')
    
    comments = post.comments.filter(status=True)
    
    user_comment = None
    
    if request.method == 'POST':
        comment_form = commentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('' + str(post.id))
    else:
        comment_form = commentForm()

    content = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'post_details.html', content) 
   
   
class CatListView(ListView):
    
    template_name = 'category.html'
    context_object_name = 'catList'
    
    def get_queryset(self):
        
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        
        return content
    
def categories_processor(request):
    categories = Category.objects.exclude(name='default')

    return {'categories': categories}
