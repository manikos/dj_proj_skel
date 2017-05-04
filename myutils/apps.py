from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MyutilsConfig(AppConfig):
    name = 'myutils'  # python path of the app. Since this app is already under project root, we just declare its name
    verbose_name = _('My utilities')
