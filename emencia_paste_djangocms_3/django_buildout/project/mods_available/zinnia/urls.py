# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^news/', include('zinnia.urls', namespace='zinnia')),
    ) + urlpatterns
