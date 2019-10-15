from urllib.parse import unquote, urlsplit

from django.contrib.staticfiles import finders
from django.conf import settings

from whitenoise.storage import CompressedManifestStaticFilesStorage


class SuperRentalsFileStorage(CompressedManifestStaticFilesStorage):

    def stored_name(self, name):
        """
        Prevent ManifestStaticFilesStorage from raising a ValueError when a
        file is not found in the manifest.json, or the manifest.json was
        never created (i.e. collectstatic was never run). This will prevent
        an incorrectly referenced static file in a template from causing
        a 500 error.
        """
        try:
            path = super().stored_name(name)
        except ValueError:
            parsed_name = urlsplit(unquote(name))
            path = parsed_name.path.strip()

        return path

    def url(self, name, force=False):
        """
        The ManifestStaticFilesStorage doesn't use hashed urls in DEBUG mode.
        As a result, using an incorrect filename in a template can silently
        fail during local development and result in an uncaught exception
        on production. This method ensures that an exception is raised in
        DEBUG mode to help identify this error during development.
        """
        if settings.DEBUG:
            if finders.find(name) is None:
                raise ValueError(
                        'The file {} could not be found with {}'
                        .format(name, self))

        return super().url(name)
