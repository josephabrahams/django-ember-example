from django.apps import AppConfig
from django.contrib.staticfiles.apps import StaticFilesConfig


class SuperRentalsConfig(AppConfig):
    name = 'superrentals'
    verbose_name = "SuperRentals"


class SuperRentalsStaticFilesConfig(StaticFilesConfig):
    ignore_patterns = ['CVS', '.*', '*~', '*.html']
