import os
from django.test.runner import DiscoverRunner
import radish.main


class RadishTestRunner(DiscoverRunner):
    features = ['features']

    def run_suite(self, suite, **kwargs):
        return radish.main.main(['features'])

    def suite_result(self, suite, result, **kwargs):
        return result

    def set_features(self, features):
        self.features = features
