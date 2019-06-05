# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class MessengerUser(models.Model):
    ps_id=models.TextField()

class FacebookPage(models.Model):
    access_token = models.TextField()
    original_id = models.TextField() # Graph id


class FacebookLabel(models.Model):
    owner = models.ForeignKey(MessengerUser)
    page = models.ForeignKey(FacebookPage,null=True)
    label_id = models.TextField(null=True)