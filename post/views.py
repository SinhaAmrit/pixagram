from django.shortcuts import render, redirect
from post.models import Tag, Stream, Follow, Post
from post.forms import NewPostForm
from django.contrib.auth.decorators import login_required


@login_required
def feed(request):
    user = request.user
    posts = Stream.objects.filter(user=user).select_related("post")

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data["picture"]
            caption = form.cleaned_data["caption"]
            tags_list = form.cleaned_data["tag"].split(",")

            tags_objs = [Tag.objects.get_or_create(title=tag)[0] for tag in tags_list]
            post = Post.objects.create(
                picture=picture, caption=caption, user=user  # Use user directly
            )
            post.tag.set(tags_objs)
            return redirect("/")
    else:
        form = NewPostForm()
        group_ids = []
        for post in posts:
            group_ids.append(post.post_id)
        post_items = Post.objects.filter(id__in=group_ids).all().order_by("-posted")
    context = {"post_items": post_items, "form": form}
    return render(request, "post/feed.html", context)
