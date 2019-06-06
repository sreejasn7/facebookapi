# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class MessengerUser(models.Model):
    ps_id = models.TextField()

    def __str__(self):
        return 'psid_{0}'.format(self.pk)


class FacebookPage(models.Model):
    access_token = models.TextField()
    original_id = models.TextField()  # Graph id

    def __str__(self):
        return 'page_{0}'.format(self.pk)


class FacebookLabel(models.Model):
    owner = models.ForeignKey(MessengerUser)
    page = models.ForeignKey(FacebookPage, null=True)
    label_id = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{0} , {1}'.format(self.owner, self.page)
