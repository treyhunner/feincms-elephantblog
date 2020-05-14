from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from elephantblog.modeladmins import CategoryAdmin, EntryAdmin
from elephantblog.models import Category
from elephantblog.utils import get_entry_model


admin.site.register(get_entry_model(), EntryAdmin)
admin.site.register(Category, CategoryAdmin)
