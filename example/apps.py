from django.contrib.staticfiles.apps import StaticFilesConfig


class ExampleStaticFilesConfig(StaticFilesConfig):
    ignore_patterns = ['CVS', '.*', '*~', '*.html']
