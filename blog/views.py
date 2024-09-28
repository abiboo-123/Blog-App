from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Post, Contact, Comment
from .forms import contactForm, commentForm
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
     