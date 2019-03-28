# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from aldryn_apphooks_config.admin import BaseAppHookConfig, ModelAppHookConfig
from aldryn_people.models import Person
from aldryn_translation_tools.admin import AllTranslationsMixin
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.forms import widgets
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple

from .cms_appconfig import RSSFeedConfig

class RSSFeedConfigAdmin(
    BaseAppHookConfig,
    TranslatableAdmin
):
    def get_config_fields(self):
        return (
            'app_title', 'title', 'description', 'feed_type', 'model',
            'section', 'limit',)


admin.site.register(RSSFeedConfig, RSSFeedConfigAdmin)
