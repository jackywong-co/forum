import uuid

from django.contrib.auth.models import Group, User
from django.db import models


class Channel(models.Model):
    status = {
        (0, 'Inactive'),
        (1, 'Active')
    }
    channel_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    channel_name = models.CharField(max_length=30, unique=True)
    channel_priority = models.IntegerField(default=50)

    status = models.SmallIntegerField(choices=status, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.channel_name


class ChannelAdminGroup(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    admin_group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Post(models.Model):
    status = {
        (0, 'Inactive'),
        (1, 'Active')
    }
    post_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    post_title = models.CharField(max_length=30)
    post_priority = models.IntegerField(default=50)
    post_content = models.TextField()

    status = models.SmallIntegerField(choices=status, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title


class PostLike(models.Model):
    post_like_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like_post = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.post_title


class Comment(models.Model):
    status = {
        (0, 'Inactive'),
        (1, 'Active')
    }
    comment_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    status = models.SmallIntegerField(choices=status, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
