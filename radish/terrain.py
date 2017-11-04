import os
import datetime
import django
import warnings
from radish import before, after, world
from django.test import LiveServerTestCase
from django.test.runner import DiscoverRunner
from selenium import webdriver


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.feature')
BASE_URL = os.environ.get('BASE_URL', 'http://localhost:8000')


@before.all
def setup_django(features, marker):
    world.start_time = datetime.datetime.now()
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    django.setup()
    world.test_runner = DiscoverRunner(interactive=False, verbosity=0)
    world.test_runner.setup_test_environment()
    world.old_db_config = world.test_runner.setup_databases()


@after.all
def tear_down_django(features, marker):
    world.test_runner.teardown_databases(world.old_db_config)
    world.test_runner.teardown_test_environment()
    elapsed_time = datetime.datetime.now() - world.start_time
    print("custom timer: " + str(elapsed_time))


@before.each_feature
def set_up_feature(feature):
    LiveServerTestCase.setUpClass()


@after.each_feature
def tear_down_feature(feature):
    LiveServerTestCase.tearDownClass()


@before.each_scenario
def set_up_scenario(scenario):
    scenario.context.test_case = LiveServerTestCase()
    scenario.context.test_case._pre_setup()
    scenario.context.browser = webdriver.Chrome()
    scenario.context.base_url = BASE_URL


@after.each_scenario
def tear_down_scenario(scenario):
    scenario.context.browser.quit()
    scenario.context.test_case._post_teardown()
