from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from markdown import markdown


class Entry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=False)
    intro = models.TextField(blank=False)
    markup = models.TextField(blank=False)
    body = models.TextField(blank=False)
    date = models.DateField(auto_now=True)
    published = models.CharField(max_length=2, choices=[
        ("d", "Draft"),
        ("p", "Published"),
    ], default="d")
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("detail", [self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.markup = markdown(self.body)

        super(Entry, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Entries"
