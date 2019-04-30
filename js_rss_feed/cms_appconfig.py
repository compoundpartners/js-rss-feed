# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from app_data import AppDataForm
from django import forms
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
try:
    from js_vacancies.models import Vacancy
    THERE_IS_VACANCY = True
except:
    THERE_IS_VACANCY = False


FEED_TYPES = (
    ('Rss201rev2Feed', 'RSS 2.01.'),
    ('RssUserland091Feed', 'RSS 0.91.'),
    ('Atom1Feed', 'Atom 1.0.'),
)
MODELS = (
    ('article', 'Article'),
    ('event', 'Event'),
)
if THERE_IS_VACANCY:
    MODELS += (
        ('vacancy', 'Vacancy'),
    )


@python_2_unicode_compatible
class RSSFeedConfig(TranslatableModel, AppHookConfig):
    translations = TranslatedFields(
        app_title=models.CharField(_('name'), max_length=234),
        title = models.CharField(
            _('feed title'), max_length=255, blank=False),
        description = models.CharField(
            _('feed description'), max_length=255, blank=False)
    )
    feed_type = models.CharField(
        _('feed type'), max_length=32,
        blank=False, default='Rss201rev2Feed', choices=FEED_TYPES)
    model = models.CharField(
            _('feed model'), max_length=32,
            blank=False, default='article', choices=MODELS)
    section = models.CharField(
        _('feed section slug'), max_length=32, blank=True, null=True)
    limit = models.PositiveIntegerField(
        _('feed limit'), blank=True, null=True)

    def get_app_title(self):
        return self.safe_translation_getter('app_title')

    class Meta:
        verbose_name = _('RSS Feed')
        verbose_name_plural = _('RSS Feeds')

    def __str__(self):
        return self.safe_translation_getter('app_title')


class RSSFeedConfigForm(AppDataForm):
    pass


setup_config(RSSFeedConfigForm, RSSFeedConfig)
