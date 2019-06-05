# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import MessengerUser , FacebookLabel , FacebookPage

# Register your models here.

admin.site.register(MessengerUser)
admin.site.register(FacebookPage)
admin.site.register(FacebookLabel)