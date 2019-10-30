# If on Python 2.X
from __future__ import print_function

import pysolr
from django.conf import settings

from solr.tasks import BaseTaskIndexing

from iati_organisation.models import Organisation
from solr.organisation.indexing import OrganisationIndexing

solr = pysolr.Solr(
    '{url}/{core}'.format(
        url=settings.SOLR.get('url'),
        core=settings.SOLR.get('cores').get('organisation')
    ), always_commit=True
)


class DatasetNoteTaskIndexing(BaseTaskIndexing):
    indexing = OrganisationIndexing
    model = Organisation
    solr = solr