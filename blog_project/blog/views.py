from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# views.py
from .forms import CommentForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save comment to the database
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Associate the logged-in user
            comment.save()
            return redirect("post_detail", slug=slug)
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
        },
    )


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the user is the comment author
    if request.user != comment.author:
        return redirect("post_detail", slug=comment.post.slug)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {"form": form, "comment": comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the user is the comment author
    if request.user != comment.author:
        return redirect("post_detail", slug=comment.post.slug)

    post_slug = comment.post.slug  # Store the post's slug before deletion
    comment.delete()
    return redirect("post_detail", slug=post_slug)


def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Redirect to the profile or dashboard after successful login
            return redirect("profile")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
