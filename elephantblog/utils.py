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
    """@return: all entries that have at least one category in common"""
    return (
        get_entry_model()
        .objects.active()
        .filter(categories__in=entry.categories.all())
        .exclude(pk=entry.pk)
        .distinct()
    )


def get_entry_model():
    return apps.get_model(*_get_entry_model_setting().split("."), require_ready=False)


def get_related_query_kwargs(**kwargs):
    res = dict()
    model_setting = _get_entry_model_setting()
    for old_kwarg, value in kwargs.items():
        # convert blogentries__isnull to app_name_model_blogentries__isnull
        kwarg = (
            "_".join(_get_entry_model_setting().split(".")).lower() + "_" + old_kwarg
        )
        res[kwarg] = value
    return res


def _get_entry_model_setting():
    return getattr(
        settings,
        "ELEPHANTBLOG_DEFAULT_ENTRY_MODEL",
        app_settings.ELEPHANTBLOG_DEFAULT_ENTRY_MODEL,
    )
