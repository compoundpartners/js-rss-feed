# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.syndication.views import Feed
from django.utils import feedgenerator
from aldryn_apphooks_config.utils import get_app_instance
from aldryn_newsblog.models import Article
from js_events.models import Event
try:
    from js_vacancies.models import Vacancy
    THERE_IS_VACANCY = True
except:
    THERE_IS_VACANCY = False



class RSSFeed(Feed):
    link = '/'
    def __call__(self, request, *args, **kwargs):
        self.namespace, self.config = get_app_instance(request)
        self.feed_type = getattr(feedgenerator, self.config.feed_type)
        self.section = request.GET.get('section', None)
        self.category = request.GET.get('category', None)
        return super(RSSFeed, self).__call__(request, *args, **kwargs)

    def title(self):
        return self.config.safe_translation_getter('title')

    def description(self):
        return self.config.safe_translation_getter('description')

    def items(self):
        if THERE_IS_VACANCY and self.config.model == 'vacancy':
            self.model = Vacancy
        elif self.config.model == 'event':
            self.model = Event
        else:
            self.model = Article
        items = self.model.objects.published().order_by('-publishing_date')
        if self.category:
            items = items.filter(categories__translations__slug=self.category)
        if self.config.section:
            items = items.filter(app_config__namespace=self.config.section)
        elif self.section:
            items = items.filter(app_config__namespace=self.section)
        items = list(items)
        if self.config.limit:
            return items[:self.config.limit]
        return items

    def item_title(self, item):
        return item.safe_translation_getter('title')

    def item_description(self, item):
        return item.safe_translation_getter('lead_in')

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.publishing_date

    def item_author_name(self, item):
        if self.config.model == 'article' and item.author:
            return item.author
        else:
            ''
    #def item_categories(self, item):
