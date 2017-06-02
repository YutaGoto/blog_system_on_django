from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 30)
    body = models.TextField(max_length = 1000)
    tags = models.ManyToManyField(Tag, through='PostsTag')

    def __str__(self):
        return self.title

class PostsTag(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)
