from django.urls import path
from post import views

urlpatterns = [
    path("", views.feed, name="feed"),
    path("post/<uuid:post_id>/like", views.like, name="like"),
]
