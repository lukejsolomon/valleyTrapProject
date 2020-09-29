from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=200, default='', blank=True)
    summary = models.CharField(max_length=200, default='', blank=True)
    summaryImage = models.ImageField(
        upload_to='xworldblog/images/', default='', blank=True)

# pageOne
    pageOneTitle = models.CharField(max_length=200, default='', blank=True)
    pageOneImage = models.ImageField(
        upload_to='xworldblog/images/', default='', blank=True)
    pageOne = models.TextField(default='', blank=True)

    def __str__(self):
        return self.title
