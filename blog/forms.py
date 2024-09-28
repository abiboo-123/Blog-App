from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact, Comment

class contactForm(ModelForm):
    
    class Meta():
        
        model = Contact
        fields = ['name', 'email', 'message']
        
class commentForm(ModelForm):
    
    class Meta():
        
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment', 'rows': 5}),
        }
