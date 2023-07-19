from django.forms import ModelForm
from .models import Comment, Contact

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'accepted', 'user', 'post' ]

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['phone_number', 'transaction', 'user', 'comment']