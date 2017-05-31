from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 30)
    body = models.TextField(max_length = 1000)

class Tag(models.Model):
    name = models.CharField(max_length = 30)

class PostsTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
