from django.db import models


class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    code = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title, self.owner}'

