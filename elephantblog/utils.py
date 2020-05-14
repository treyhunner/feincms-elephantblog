from __future__ import absolute_import, unicode_literals

from django.apps import apps
from django.conf import settings
from django.utils.module_loading import import_string

import elephantblog.default_settings as app_settings


def entry_list_lookup_related(entry_qs):
    if hasattr(settings, "BLOG_LOOKUP_CLASS"):
        LookupClass = import_string(settings.BLOG_LOOKUP_CLASS)
    else:
        from .transforms import RichTextMediaFileAndCategoriesLookup as LookupClass
    LookupClass.lookup(entry_qs)


def same_category_entries(entry):
    """ @return: all entries that have at least one category in common """
    return (
        get_entry_model().objects.active()
        .filter(categories__in=entry.categories.all(),)
        .exclude(pk=entry.pk)
        .distinct()
    )


def get_entry_model():
    return apps.get_model(*app_settings.ELEPHANTBLOG_DEFAULT_ENTRY_MODEL.split('.'), require_ready=False)
