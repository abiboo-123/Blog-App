from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

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
    content = models.TextField()
    status =models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    mewmanager = NewManager()
    
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
    
    