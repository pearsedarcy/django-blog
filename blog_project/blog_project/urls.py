"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.post_list, name="post_list"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("comment/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path(
        "comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"
    ),
    path("login/", views.loginView, name="login"),
    # path("profile/", views.ProfileView.as_view(), name="profile"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
]


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
