import logging

from django.db.models import Q
from django.core.management.base import BaseCommand

from payu.models import PayUIDN

logger = logging.getLogger(__name__)


def string_to_list(list_as_string):
    return list(map(int, list_as_string.strip('[] ').split(',')))


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument(
            '--idns',
            help='A list of idns pks to be sent.',
            action='store', dest='idns', type=string_to_list
        )

    def handle(self, *args, **options):
        idns = PayUIDN.objects.filter(Q(sent=False) | Q(sent=True, success=False))

        if options['idns']:
            idns = idns.filter(pk__in=options['idns'])

        for idn in idns:
            idn.send()

            if not idn.success:
                logger.error('Encountered exception while processing idn'
                             'with id=%s, ex=%s.', idn.id, idn.response,
                             exc_info=True)
