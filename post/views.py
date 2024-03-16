from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from post.models import Tag, Stream, Follow, Post, Likes
from post.forms import NewPostForm
from django.contrib.auth.decorators import login_required


@login_required
def feed(request):
    user = request.user
    user_id = request.user.id
    posts = Stream.objects.filter(user=user).select_related("post")
    tags_objs = []
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get("picture")
            caption = form.cleaned_data.get("caption")
            tag_form = form.cleaned_data.get("tag")
            tags_list = list(tag_form.split(","))
            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
            p, created = Post.objects.get_or_create(
                picture=picture, caption=caption, user_id=user_id
            )
            p.tag.set(tags_objs)
            p.save()
            return redirect("/")
    else:
        form = NewPostForm()
        group_ids = []
        for post in posts:
            group_ids.append(post.post_id)
        post_items = Post.objects.filter(id__in=group_ids).all().order_by("-posted")
    context = {"post_items": post_items, "form": form}
    return render(request, "post/feed.html", context)


@login_required
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()
    if not liked:
        liked = Likes.objects.create(user=user, post=post)
        current_likes += 1
    else:
        liked = Likes.objects.filter(user=user, post=post).delete()
        current_likes = max(0, current_likes - 1)
    post.likes = current_likes
    post.save()
    return redirect("/")
