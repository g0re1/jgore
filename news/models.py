from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.title