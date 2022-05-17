from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class ContactForm(forms.ModelForm):
    class Meta:
            model = Contact
            fields = ('name','subject', 'message','sender', 'cc_myself',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

""" No creé un formulario para usuarios porque no le encontré sentido si Django ya tiene uno.
En reemplazo hice el de post """
