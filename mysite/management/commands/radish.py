from __future__ import absolute_import
import sys
from django.core.management.base import BaseCommand, CommandError
from mysite.test.runner import RadishTestRunner

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('features', nargs='+', type=str)

    def handle(self, *test_labels, **options):
        test_runner = RadishTestRunner(interactive=False)
        if options['features']:
            test_runner.set_features(options['features'])
        result = test_runner.run_suite(None)
        if result:
            sys.exit(result)
