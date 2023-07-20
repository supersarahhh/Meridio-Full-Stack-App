from django.forms import ModelForm, CharField
from django import forms
from .models import Comment, Contact

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'accepted', 'user', 'post']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'