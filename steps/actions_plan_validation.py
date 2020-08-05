import datetime
import locale
import math
import time
from utils.salesforce import soql
from datetime import datetime
import re
import unittest
import dateutil

from behave import step, then
from nose.tools import assert_equals, assert_false

from pages.home_page import HomePage


@step(u'I verify the actions plan is present')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(10)
    driver = context.driver
    parser = context.parser
    home = HomePage(driver)
    home.wait_for_new_segment_button(15)
    # context.segment_info = {'name': 'Automation 20200803151704', 'closed opportunities': '711,780', 'users included': '12', 'industry': 'Banking'}
    name = context.segment_info.get("name")
    driver.refresh()
    print(context.segment_info)
    print("checking that segment is present")
    assert home.is_segment_present(name)
    home.select_segment(name)

    assert_equals(parser.get('Home', 'Home tab1'), driver.find_element(*home.home_tab_op1).text)
    assert_equals(parser.get('Home', 'Home tab2'), driver.find_element(*home.home_tab_op2).text)
    assert_equals(parser.get('Home', 'Home tab3'), driver.find_element(*home.home_tab_op3).text)
    assert_equals(parser.get('Home', 'Segment label'), driver.find_element(*home.segment_label).text)
    assert_equals(parser.get('Home', 'New Segment button'), driver.find_element(*home.new_segment).text)
    assert_equals(parser.get('Home', 'Delete Segment button'), driver.find_element(*home.delete_segment_bnt).text)
    assert_equals(parser.get('Home', 'Industry Label'), driver.find_element(*home.industry_label).text)
    assert_equals(parser.get('Home', 'Sales Label'), driver.find_element(*home.sales_label).text)
    assert_equals(parser.get('Home', 'Won Label'), driver.find_element(*home.won_label).text)
    assert_equals(parser.get('Home', 'Average Sales Label'), driver.find_element(*home.average_sales_label).text)
    assert_equals(parser.get('Home', 'Sales kpi'), driver.find_element(*home.sales_kpi_label).text)
    current_month = datetime.now()
    previous_month = current_month + dateutil.relativedelta.relativedelta(months=-1)
    month_label = previous_month.strftime("%B")
    assert_equals(month_label + " " + parser.get('Home', 'Month Summary'),
                  driver.find_element(*home.month_summary_label).text)
    assert_equals(parser.get('Home', 'Average Sales Per Rep'), driver.find_element(*home.average_sales_rep_label).text)
    assert_equals(parser.get('Home', 'Win Rate Label'), driver.find_element(*home.win_rate_label).text)
    assert_equals(parser.get('Home', 'Days to Close'), driver.find_element(*home.days_close_label).text)
    assert_equals(parser.get('Home', 'Sales Count'), driver.find_element(*home.sales_count_label).text)

    # checking actions plans static elements
    print(month_label+"'s Action Plans")
    assert_equals(month_label+"'s Action Plans", driver.find_element(*home.action_plan_label).text)
    actions_plans = home.get_actions_plans()
    context.segment_info["month_action_plan"] = actions_plans
    print(actions_plans)
    for plan in actions_plans:
        assert_equals(month_label + " " + previous_month.strftime("%Y"), plan.get("date"))
        assert_equals(parser.get('Home', 'Action plan not started'), plan.get("status"))
        assert color_match(plan.get("kpi text"),plan.get("kpi class"))



@step(u'I change the status of the action plan')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(3)
    driver = context.driver
    parser = context.parser
    home = HomePage(driver)
    home.wait_for_new_segment_button(15)
    actions_plans = home.get_actions_plans()
    print(actions_plans)
    for line in context.table:
        kpi = line["KPI"]
        status = line["New status"]
        row = 1
        for element in actions_plans:
            if kpi in element.get("kpi text"):
                print("entro en el if para el kpi: "+kpi)
                home.change_action_plan_status(row, status)
                for action in context.segment_info["month_action_plan"]:
                    if kpi in action.get("kpi text"):
                        action["status"] = status
            row = row + 1
    print(context.segment_info["month_action_plan"])

def color_match(kpi_text, kpi_class):
    """return true or false accorting posivie green and negative red"""
    positive = re.compile('.*\s[1-9]%.*|.*\s[1-9][0-9]%.*|.*\s(100)%.*|')
    negative = re.compile('.*-[1-9]%.*|.*-[1-9][0-9]%.*|.*-(100)%.*|')
    if positive.match(kpi_text) and "positive" in kpi_class:
        return True
    elif negative.match(kpi_text) and "negative" in kpi_class:
        return True
    else:
        return False


@step("now I iterate to the status selector checking the status change")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(3)
    driver = context.driver
    parser = context.parser
    home = HomePage(driver)
    home.wait_for_new_segment_button(15)

    current_month = datetime.now()
    previous_month = current_month + dateutil.relativedelta.relativedelta(months=-1)
    month_label = previous_month.strftime("%B")
    status_list = [month_label + parser.get('Home', 'Month action plan'), parser.get('Home', 'All action plan'), parser.get('Home', 'Action plan not started'), parser.get('Home', 'Action plan in progress'), parser.get('Home', 'Action plan completed') ]
    all_actions_plans = context.segment_info["month_action_plan"]

    for status in status_list:

        if status == parser.get('Home', 'All action plan'):
            home.select_status(status)
            time.sleep(2)
            home.driver.find_element(*home.refresh_button).click()
            time.sleep(2)
            current_action_plan = home.get_actions_plans()
            assert_equals(current_action_plan, all_actions_plans)
        elif status == month_label + parser.get('Home', 'Month action plan'):
            current_action_plan = home.get_actions_plans()
            expected_action_plans = list(filter(lambda action: action.get("status") != "Dismiss", all_actions_plans))
            assert_equals(current_action_plan, expected_action_plans)

        else:
            home.select_status(status)
            time.sleep(2)
            home.driver.find_element(*home.refresh_button).click()
            time.sleep(2)
            current_action_plan = home.get_actions_plans()
            expected_action_plans = list(filter(lambda action: action.get("status") == status, all_actions_plans))
            assert_equals(current_action_plan, expected_action_plans)


