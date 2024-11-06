from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 6,
                "placeholder": "Add a comment...",
                "class": "textarea textarea-bordered w-full textarea-secondary",
            }
        ),
        label="",
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "cover_image",
        ]  # Excluding 'slug' and 'author' since these will be handled automatically

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 6,
                "placeholder": "Add a comment...",
                "class": "textarea textarea-bordered w-full textarea-secondary",
            }
        ),
        label="",
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "input input-bordered w-full input-secondary",
            }
        ),
        label="",
    )
    cover_image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "file-input file-input-bordered w-full file-input-secondary",
            }
        ),
        label="Cover Image",
    )
