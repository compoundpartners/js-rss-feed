# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .cms_appconfig import RSSFeedConfig


class RSSFeedApp(CMSConfigApp):
    name = _('RSS Feed')
    app_name = 'js_rss_feed'
    app_config = RSSFeedConfig

    def get_urls(self, *args, **kwargs):
        return ['js_rss_feed.urls']

apphook_pool.register(RSSFeedApp)
