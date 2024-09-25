from django.shortcuts import render, redirect
from .models import Post, Contact
from .forms import contactForm
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
    
    content = {'post': post}
    
    return render(request, 'post_details.html', content) 
     