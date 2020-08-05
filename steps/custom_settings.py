# -*- coding: UTF-8 -*-
import time
from behave import given, then
from nose.tools import assert_equals
from pages.custom_setting_page import CustomSettingsPage
from pages.tabs_bar import TabsBar


@given(u'navigate into Custom Settings')
def step_impl(context):
    driver = context.driver
    tab_bar = TabsBar(driver)
    tab_bar.wait_for_bar(30)
    tab_bar.navigate_to("app settings")


@then(u'bla bla')
def step_impl(context):
    time.sleep(30)


@then("I validate verify the app configuration is according to this table")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    custom_settings = CustomSettingsPage(driver)
    custom_settings.navigate_to_app_settings()
    # Checking the static content as title and labels
    assert_equals(parser.get('Custom Settings', 'Title'),
                  driver.find_element(*CustomSettingsPage.title).text)
    assert_equals(parser.get('Custom Settings', 'Name label'),
                  driver.find_element(*CustomSettingsPage.name_label).text)
    assert_equals(parser.get('Custom Settings', 'Allow Effectiveness label'),
                  driver.find_element(*CustomSettingsPage.allow_effectiveness_label).text)
    assert_equals(parser.get('Custom Settings', 'Cron benchmark label'),
                  driver.find_element(*CustomSettingsPage.cron_benchmark_label).text)
    assert_equals(parser.get('Custom Settings', 'Cron Expression Snapshot Job label'),
                  driver.find_element(*CustomSettingsPage.cron_snapshot_job_label).text)
    assert_equals(parser.get('Custom Settings', 'Fiscal year opt in label'),
                  driver.find_element(*CustomSettingsPage.fiscal_year_opt_label).text)
    assert_equals(parser.get('Custom Settings', 'Opt in label'),
                  driver.find_element(*CustomSettingsPage.opt_in).text)
    assert_equals(parser.get('Custom Settings', 'Allow benchmarking label'),
                  driver.find_element(*CustomSettingsPage.allow_benchmark_label).text)
    assert_equals(parser.get('Custom Settings', 'Async reports label'),
                  driver.find_element(*CustomSettingsPage.async_report_label).text)
    assert_equals(parser.get('Custom Settings', 'Cron Snapshot job label'),
                  driver.find_element(*CustomSettingsPage.cron_send_snapshot_label).text)
    assert_equals(parser.get('Custom Settings', 'Customer key label'),
                  driver.find_element(*CustomSettingsPage.customer_key_label).text)
    assert_equals(parser.get('Custom Settings', 'Test Org label'),
                  driver.find_element(*CustomSettingsPage.test_org_label).text)
    assert_equals(parser.get('Custom Settings', 'Regression label'),
                  driver.find_element(*CustomSettingsPage.use_regression_label).text)
    # Checking the input values according expected in step table
    for line in context.table:
        name = line["Name"]
        allow_benchmark = line["Allow Benchmarking"]
        async_report = line["Async Reports"]
        cron_benchmark = line["Cron Benchmark"]
        cron_send_snapshot = line["Cron Send Snapshot"]
        cron_snapshot_job = line["Cron Snapshot Job"]
        opt_in = line["Opt In"]
        regression_formula = line["Regression Formula"]
        assert_equals(name, driver.find_element(*CustomSettingsPage.app_settings_value).text)
        assert_equals(allow_benchmark,
                      custom_settings.is_checked(driver.find_element(*CustomSettingsPage.allow_benchmark_checkbox)))
        assert_equals(cron_benchmark, driver.find_element(*CustomSettingsPage.cron_benchmark_value).text)
        assert_equals(cron_send_snapshot, driver.find_element(*CustomSettingsPage.cron_send_snapshot_value).text)
        assert_equals(cron_snapshot_job, driver.find_element(*CustomSettingsPage.cron_snapshot_job_value).text)
        assert_equals(allow_benchmark,
                      custom_settings.is_checked(driver.find_element(*CustomSettingsPage.allow_benchmark_checkbox)))
        assert_equals(async_report,
                      custom_settings.is_checked(driver.find_element(*CustomSettingsPage.async_report_checkbox)))
        assert_equals(regression_formula,
                      custom_settings.is_checked(driver.find_element(*CustomSettingsPage.use_regression_checkbox)))
        assert_equals(opt_in, custom_settings.is_checked(driver.find_element(*CustomSettingsPage.opt_in_checkbox)))
