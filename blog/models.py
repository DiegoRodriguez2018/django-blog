from django.db import models
from django.urls import reverse 

# Create your models here.

#Note that Post is inheriting from models.Model
class Post(models.Model):
    title =models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

#we add a subclas called Meta
    class Meta:
        ordering = ['-created']
    def __unicode__(self):
        return u'%s'% self.title
    def get_absolute_url(self):
        return reverse('blog.view.post', args=[self.slug])

