from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escreva seu comentário aqui...'})
        }