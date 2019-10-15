import json
import os
import urllib

from django.conf import settings
from django.http import HttpResponse, Http404
from django.template import loader

from pyquery import PyQuery as pq
from rest_framework import viewsets

from .models import Rental
from .serializers import RentalSerializer


def ember(request, **kwargs):
    index_file = 'static/index.html'
    index_file_path = os.path.join(settings.DJANGO_ROOT, index_file)

    if not os.path.isfile(index_file_path):
        raise Http404('{} does not exist. Make sure to build the '
                      ' Ember app before visiting this page.'
                      .format(index_file))

    ember = pq(filename=index_file_path)
    encoded_config = ember(
            '[name="superrentals/config/environment"]').attr['content']
    config = json.loads(urllib.parse.unquote(encoded_config))
    config.update(settings.EMBER_CONFIG)
    context = {'config': urllib.parse.quote(json.dumps(config)),
               'lr_enabled': settings.LIVERELOAD_ENABLED,
               'lr_port': settings.LIVERELOAD_PORT}
    content = loader.render_to_string('index.html', context)

    return HttpResponse(content)


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    http_method_names = ['get', 'head', 'options']
    ordering_fields = ('title', 'owner', 'city', 'category', 'bedrooms',)
    rels = ('exact', 'iexact', 'contains', 'icontains',
            'gt', 'gte', 'lt', 'lte', 'in', 'regex', 'isnull',)
    filterset_fields = {
        'title': rels,
        'owner': rels,
        'city': rels,
        'category': rels,
        'bedrooms': rels,
    }
