import os
import allure
from configparser import ConfigParser
from utils.webdriverfactory import WebDriverFactory


def before_all(context):
    print('Before all started')

    # Here we get all the flags from cli
    context.headless = context.config.userdata.get("headless", "no")
    context.browser = context.config.userdata.get("browser", "chrome")
    context.language = context.config.userdata.get("language", "english")

    #credentials and env as cli argument
    context.org_url = context.config.userdata.get("url")
    context.admin_credentials = context.config.userdata.get("admin")
    context.security_token = context.config.userdata.get("security_token")
    context.admin_password = context.config.userdata.get("adminpass")

    context.sales_user_credentials = context.config.userdata.get("user", "english")
    context.sales_user_password = context.config.userdata.get("userpass", "pass")

    # Here we get load a property file according the language of our test
    context.parser = ConfigParser()
    print("loading properties according language: " + context.language)
    context.parser.read((os.path.join(os.getcwd(), 'utils/languages/')) + context.language + ".ini")


def before_scenario(context, scenario):
    print('New scenario started: ')
    print(scenario)
    if 'ui' in scenario.tags:
        print("Setting up browser for UI test")
        wd = WebDriverFactory(context.browser)
        context.driver = wd.get_web_driver_instance(context.headless)


def after_scenario(context, scenario):
    print('scenario has been finished')
    if 'ui' in scenario.tags:
        print("closing the browser")
        if scenario.status == "failed":
            print('screen capture required by sys parameters')
            allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
        print(
            "=========================================================================================================")
        context.driver.quit()



