from django.contrib import admin

from .models import Post, PostsTag, Tag

class PostsTagInline(admin.TabularInline):
    model = PostsTag
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostsTagInline]
    list_display = ('title', '_tags')

    def _tags(self, post):
        return ','.join([tag.name for tag in post.tags.all()])

class TagAdmin(admin.ModelAdmin):
    inlines = [PostsTagInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
