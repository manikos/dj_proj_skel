from django.contrib import sitemaps
from django.urls import reverse


class MyModelSitemap(sitemaps.Sitemap):
    changefreq = 'yearly'
    priority = 0.6
    i18n = True

    def items(self):
        return MyModel.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = 'yearly'
    priority = 0.5
    i18n = True

    def items(self):
        return ['url_names_of_static_pages']

    def location(self, obj):
        return reverse(obj)


SITEMAPS = {
    'mymodels': MyModelSitemap,
    'static': StaticViewSitemap
}
