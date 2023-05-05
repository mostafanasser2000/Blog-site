from django import forms
from django.forms import ModelForm
from .models import Post
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['title'].label = ''
        
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'Content'
        self.fields['content'].widget.attrs['rows'] = '5'

        self.fields['content'].label = ''
        
        self.fields['categories'].label = 'Post Categories (hold ctrl and select for multiple)'
        self.fields['categories'].widget.attrs['class'] = 'form-select form-select-lg'
        
        self.fields['image'].label = 'Post Image'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['title'] = 'Select image for post'

        
        
        
        
     
