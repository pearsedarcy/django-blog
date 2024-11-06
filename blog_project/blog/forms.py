from django import forms
from .models import Comment


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
