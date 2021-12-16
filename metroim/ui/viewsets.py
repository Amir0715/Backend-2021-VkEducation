from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_GEO_DISTANCE,
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from ui.documents import StationDocument
from ui.serializers import StationDocumentSerializer


class StationDocumentView(BaseDocumentViewSet):
    document = StationDocument
    serializer_class = StationDocumentSerializer
    pagination_class = PageNumberPagination

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        # OrderingFilterBackend,
        # DefaultOrderingFilterBackend,
        SuggesterFilterBackend,
        SearchFilterBackend
    ]

    # Define search fields
    search_fields = (
        'name',
        'city',
        'line',
    )

    filter_fields = {
        'id': {
            'field': 'id',
            # Note, that we limit the lookups of id field in this example,
            # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'name': 'name.raw',
        'line': 'line.raw',
        'city': 'city.raw',
    }

    suggester_fields = {
        'name_suggest': {
            'field': 'name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
        'city_suggest': {
            'field': 'city.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
        'line_suggest': {
            'field': 'line.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        }
    }

    # # Define ordering fields
    # ordering_fields = {
    #     'id': None,
    #     'name': None,
    #     'city': None,
    #     'line': None,
    # }

    # # Specify default ordering
    # ordering = ('id', 'name',)

    geo_spatial_filter_fields = {
        'location': {
            'lookups': [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }
