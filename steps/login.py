# -*- coding: UTF-8 -*-
import time
from behave import given
from pages.login_page import LoginPage


@given(u'I successfully login in Salesforce using "{text}" credentials')
def step_impl(context, text):
    driver = context.driver
    url = context.org_url
    context.current_role = text
    if text == "Admin":
        username = context.admin_credentials
        password = context.admin_password
    else:
        username = context.sales_user_credentials
        password = context.sales_user_password
    print(url)
    print(username)
    print(password)
    driver.get(url)
    login = LoginPage(driver)
    login.wait_for_input(10)
    login.do_login(username, password)
    time.sleep(15)
