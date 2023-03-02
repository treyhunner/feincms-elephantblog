from django.contrib.sitemaps import Sitemap

from elephantblog.utils import get_entry_model


class EntrySitemap(Sitemap):
    def items(self):
        return get_entry_model().objects.active()

    def lastmod(self, obj):
        return obj.last_changed
