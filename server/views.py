import os

from django.conf import settings
from django.http import HttpResponse
from django.template import loader

from pyquery import PyQuery as pq


def client(request):

    ember = pq(filename=os.path.join(settings.DJANGO_ROOT,
                                     'static/client/index.html'))
    config = ember('[name="app/config/environment"]').attr['content']
    context = {'config': config,
               'lr_enabled': settings.LIVERELOAD_ENABLED,
               'lr_port': settings.LIVERELOAD_PORT,}
    content = loader.render_to_string('client/index.html', context)

    return HttpResponse(content)
