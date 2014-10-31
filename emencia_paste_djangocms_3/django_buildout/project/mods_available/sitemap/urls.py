# -*- coding: utf-8 -*-
"""
Here we bind Sitemap containers for each available apps and ressources

This default config is made to support DjangoCMS, Zinnia, Porticus and staticpages, 
only DjangoCMS is enabled, uncomment the others or add new app ressources for your 
needs (see the Django sitemap documentation for more details)
"""
from django.conf import settings
from django.core.urlresolvers import reverse

#from project.contact_form.sitemaps import ContactFormEntryBase, ContactFormSitemapBase

from cms.sitemaps import CMSSitemap

#from zinnia.sitemaps import TagSitemap
#from zinnia.sitemaps import EntrySitemap
#from zinnia.sitemaps import CategorySitemap
#from zinnia.sitemaps import AuthorSitemap

from staticpages.sitemaps import StaticPageSitemapAuto

#from porticus.models import Album
#from porticus.sitemaps import PorticusAlbumSitemap


#class BookingFormEntry(ContactFormEntryBase):
    #"""Booking form entry for Contact forms sitemap"""
    #url_name = 'booking_form'

#class ContactFormSitemap(ContactFormSitemapBase):
    #"""Contact forms sitemap"""
    #contact_forms = [BookingFormEntry]


#class PrototypesSitemap(StaticPageSitemapAuto):
    #"""Prototypes sitemap"""
    #pages_map = settings.STATICPAGES_PROTOTYPES


#class PorticusAlbumVisiteSitemap(PorticusAlbumSitemap):
    #"""
    #Custom Porticus album sitemap to only display the Album 'Visite'
    #"""
    #priority = 1.0
    
    #def items(self):
        #return Album.objects.filter(slug="visite").order_by('priority', 'name')
    
    #def location(self, obj):
        #return reverse('porticus-visite-album-detail')


# Enabled sitemaps
sitemaps = {
    ## For Porticus
    #'albums': PorticusAlbumVisiteSitemap,
    ## For Contact forms
    #'contact': ContactFormSitemap,
    # For DjangoCMS
    'cmspages': CMSSitemap,
    # For Zinnia
    ###'tags': TagSitemap,
    #'blog': EntrySitemap,
    ###'authors': AuthorSitemap,
    #'categories': CategorySitemap,
    
    ## For Prototypes 
    ## WARNING: This should not be enabled in production
    #'prototypes': PrototypesSitemap,
}


# Full sitemap
urlpatterns += patterns('django.contrib.sitemaps.views',
    url(r'^sitemap\.xml$', 'sitemap', {'sitemaps': sitemaps}),
) + urlpatterns

## Sitemap divised into an index + sections
#urlpatterns += patterns('django.contrib.sitemaps.views',
    #url(r'^sitemap.xml$', 'index', {'sitemaps': sitemaps}),
    #url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
#) + urlpatterns
