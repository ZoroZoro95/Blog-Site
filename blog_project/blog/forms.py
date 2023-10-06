from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Blog Author','Blog title', 'Blog Text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'user': forms.TextInput(attrs={'class': 'textinputclass'}),
            'Comment text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
