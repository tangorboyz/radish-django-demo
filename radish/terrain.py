from radish import world, before, after
from selenium import webdriver


@before.all
def set_up(features, marker):
    world.live_server = world.get_live_server()


@after.all
def tear_down(features, marker):
    world.live_server.tearDownClass()


@before.each_scenario
def set_up_scenario(scenario):

    scenario.context.browser = webdriver.Chrome()
    scenario.context.base_url = world.live_server.live_server_url

    scenario.context.test_case = world.live_server()
    scenario.context.test_case._pre_setup()


@after.each_scenario
def tear_down_scenario(scenario):
    scenario.context.test_case._post_teardown()
    scenario.context.browser.quit()
