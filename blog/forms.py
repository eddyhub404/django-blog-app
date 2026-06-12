from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'image', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():

            if name == 'is_published':
                field.widget.attrs.update({
                    'class': 'h-4 w-4'
                })

            elif name == 'content':
                field.widget.attrs.update({
    'class': 'w-full border border-slate-600 bg-slate-900 text-white rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
    'rows': 8
})

            else:
                field.widget.attrs.update({
                    'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-gray-800'
                })

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-gray-800',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            })
        }
        
