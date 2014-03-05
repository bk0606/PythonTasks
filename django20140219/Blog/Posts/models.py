from django.db import models

class Post(models.Model):
    postTitle = models.CharField(max_length=255)
    postTime = models.DateTimeField()
    postBody = models.TextField()
    def __unicode__(self):
        return self.postTitle