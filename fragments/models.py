from django.db import models
from django.contrib.auth.models import User
from fragments.conf import app_settings

class Fragment(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=80)
    summary = models.CharField(max_length=140)
    syntax = models.CharField(max_length=80, blank=True, null=True,
                           choices=app_settings.FRAGMENTS_AVAILABLE_LANGUAGES)
    preview = models.TextField(blank=True, null=True)
    is_private = models.BooleanField(default=False)

    current_changeset = models.CharField(max_length=40, editable=False)
    current_summary = models.CharField(max_length=140, editable=False)
    
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s's fragment: %s" % (self.user.username, self.id)

    @models.permalink
    def get_absolute_url(self):
        return ('fragments_fragment_detail', (self.secret_id,))
