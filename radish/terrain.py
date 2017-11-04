import os
import django
import warnings
import datetime
from radish import before, after, world
from django.test import LiveServerTestCase
from django.test.runner import DiscoverRunner
from selenium import webdriver


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.feature')
BASE_URL = os.environ.get('BASE_URL', 'http://localhost:8000')


@before.all
def start_timer(features, marker):
    world.start_time = datetime.datetime.now()
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    django.setup()


@after.all
def stop_timer(features, marker):
    elapsed = datetime.datetime.now() - world.start_time
    print("custom timer: " + str(elapsed))


@before.each_scenario
def set_up_scenario(scenario):
    scenario.context.test_runner = DiscoverRunner(interactive=False, verbosity=0)
    scenario.context.test_runner.setup_test_environment()
    scenario.context.old_db_config = scenario.context.test_runner.setup_databases()
    scenario.context.test_class = LiveServerTestCase
    scenario.context.test_class.setUpClass()
    scenario.context.test_case = scenario.context.test_class()
    scenario.context.test_case._pre_setup()
    scenario.context.browser = webdriver.Chrome()
    scenario.context.base_url = BASE_URL


@after.each_scenario
def tear_down_scenario(scenario):
    scenario.context.browser.quit()
    scenario.context.test_case._post_teardown()
    scenario.context.test_class.tearDownClass()
    scenario.context.test_runner.teardown_databases(scenario.context.old_db_config)
    scenario.context.test_runner.teardown_test_environment()
