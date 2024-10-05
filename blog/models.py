from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

def userDirPath(instance, filename):
    return 'post/{0}/{1}'.format(instance.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    
    title = models.CharField(max_length=255)
    publishDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    content = models.TextField()
    status =models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    mewmanager = NewManager()
    image = models.ImageField(upload_to=userDirPath, default='posts/default.jpeg')
    
    class Meta():
        ordering = ('-publishDate', )
    
    def __str__(self):
        return f'{self.title} is {self.status}'
    
class Contact(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    contactDate = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)
    
    class Meta():
        ordering = ('-contactDate',)
    
    def __str__(self):
        
        if self.seen: 
            return f'{self.name}: reviewed'
        else:
            return f'{self.name}: not reviewed'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    publishDate = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ("-publishDate", )
    
    def __str__(self):
        return f'Comment by {self.name} for {self.post.title} post'
    
