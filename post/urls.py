from django.urls import path
from post import views

urlpatterns = [
    path("", views.feed, name="feed"),
    # path("create-post", views.createPost, name="create-post"),
]
