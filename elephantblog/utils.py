from __future__ import absolute_import, unicode_literals

from django.apps import apps
from django.conf import settings
from django.utils.module_loading import import_string

import elephantblog.default_settings as app_settings
from .models import Entry


if hasattr(settings, "BLOG_LOOKUP_CLASS"):
    LookupClass = import_string(settings.BLOG_LOOKUP_CLASS)
else:
    from .transforms import RichTextMediaFileAndCategoriesLookup as LookupClass


def entry_list_lookup_related(entry_qs):
    LookupClass.lookup(entry_qs)


def same_category_entries(entry):
    """ @return: all entries that have at least one category in common """
    return (
        Entry.objects.active()
        .filter(categories__in=entry.categories.all(),)
        .exclude(pk=entry.pk)
        .distinct()
    )


def get_entry_model():
    return apps.get_model(*app_settings.ELEPHANTBLOG_DEFAULT_ENTRY_MODEL.split('.'), require_ready=False)
