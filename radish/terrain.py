import os
import django
import warnings
import datetime
from radish import before, after, world
from django.test import LiveServerTestCase
from django.test.runner import DiscoverRunner
from selenium import webdriver


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.base')


@before.all
def start_timer(features, marker):
    world.start_time = datetime.datetime.now()
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    django.setup()
    world.test_runner = DiscoverRunner(interactive=False, verbosity=0)
    world.test_runner.setup_test_environment()
    world.old_db_config = world.test_runner.setup_databases()
    world.live_server = LiveServerTestCase
    world.live_server.setUpClass()


@after.all
def stop_timer(features, marker):
    world.live_server.tearDownClass()
    world.test_runner.teardown_databases(world.old_db_config)
    world.test_runner.teardown_test_environment()
    elapsed = datetime.datetime.now() - world.start_time
    print("custom timer: " + str(elapsed))


@before.each_scenario
def set_up_scenario(scenario):
    scenario.context.test_case = world.live_server()
    scenario.context.test_case._pre_setup()
    scenario.context.browser = webdriver.Chrome()
    scenario.context.base_url = world.live_server.live_server_url()


@after.each_scenario
def tear_down_scenario(scenario):
    scenario.context.browser.quit()
    scenario.context.test_case._post_teardown()
