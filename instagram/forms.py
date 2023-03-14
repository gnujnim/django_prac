from django import forms 
from .models import Post 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['photo', 'caption', 'location']
        widget = {
            'caption' : forms.Textarea,
        }