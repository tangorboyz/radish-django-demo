import os
from django.test.runner import DiscoverRunner
import radish.main


class RadishTestRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        # run unittest
        if os.getenv('RADISH_ONLY') == '1':
            result = None
            radish.main.main(['features'])
        else:
            result = super().run_suite(suite, **kwargs)
        return result

    def suite_result(self, suite, result, **kwargs):
        return 0 if result is None else super().suite_result(
            suite, result, **kwargs)
