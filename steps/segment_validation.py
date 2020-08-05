import datetime
import locale
import math
import time
from utils.salesforce import soql
from datetime import datetime

import dateutil

from behave import step, then
from nose.tools import assert_equals, assert_false

from pages.home_page import HomePage


@then("I verify the segment is present and I delete it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(3)
    driver = context.driver
    home = HomePage(driver)
    home.wait_for_new_segment_button(15)
    name = context.segment_info.get("name")
    assert home.is_segment_present(name)
    home.delete_segment(name)
    print("checking that the segment is not longer present")
    assert_false(home.is_segment_present(name))


@step(u'I verify the segment is created properly according the creation scenario')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(10)
    driver = context.driver
    parser = context.parser
    home = HomePage(driver)
    home.wait_for_new_segment_button(15)
    # context.segment_info = {'name': 'Automation 20200803171059', 'closed opportunities': '711,780', 'users included': '12', 'industry': 'Banking'}
    name = context.segment_info.get("name")
    driver.refresh()
    print(context.segment_info)
    print("checking that segment is present")
    assert home.is_segment_present(name)
    home.select_segment(name)
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
    assert_equals(month_label+" "+parser.get('Home', 'Month Summary'), driver.find_element(*home.month_summary_label).text)
    assert_equals(parser.get('Home', 'Average Sales Per Rep'), driver.find_element(*home.average_sales_rep_label).text)
    assert_equals(parser.get('Home', 'Win Rate Label'), driver.find_element(*home.win_rate_label).text)
    assert_equals(parser.get('Home', 'Days to Close'), driver.find_element(*home.days_close_label).text)
    assert_equals(parser.get('Home', 'Sales Count'), driver.find_element(*home.sales_count_label).text)
    assert_equals(parser.get('Home', 'Home tab1'), driver.find_element(*home.home_tab_op1).text)
    assert_equals(parser.get('Home', 'Home tab2'), driver.find_element(*home.home_tab_op2).text)
    assert_equals(parser.get('Home', 'Home tab3'), driver.find_element(*home.home_tab_op3).text)

    print("checking KPI")
    locale.setlocale(locale.LC_ALL, 'en_US')

    print("industry")
    assert_equals(context.segment_info.get("industry"), driver.find_element(*home.industry_value).text)

    print("sales")
    data = soql(context, "Select SUM(Amount) from Opportunity where CloseDate = LAST_N_MONTHS:1")
    assert_equals("$"+locale.format_string("%.2f", dict(data["records"][0]).get("expr0"), grouping=True),
                  driver.find_element(*home.sales_value).text)

    print("won opp")
    data = soql(context, "Select count() from Opportunity where CloseDate = LAST_N_MONTHS:1 and IsWon = true")
    assert_equals(locale.format_string("%d", data['totalSize'], grouping=True), driver.find_element(*home.won_value).text)

    print("Average Sales Size")
    data = soql(context, "Select AVG(Amount) from Opportunity where CloseDate = LAST_N_MONTHS:1")
    assert_equals("$"+locale.format_string("%.2f", dict(data["records"][0]).get("expr0"), grouping=True),
                  driver.find_element(*home.average_sales_value).text)

    print("Average Sales Per Rep")
    print(driver.find_element(*home.average_sales_rep_value).text)
    data = soql(context, "Select SUM(Amount) from Opportunity where CloseDate = LAST_N_MONTHS:1")
    sales = dict(data["records"][0]).get("expr0")
    rep = int(context.segment_info.get("users included"))
    total = sales/rep
    assert_equals("$"+locale.format_string("%.2f", total, grouping=True), driver.find_element(*home.average_sales_rep_value).text)

    print("win rate")
    data = soql(context, "Select id from Opportunity where CloseDate = LAST_N_MONTHS:1 and IsWon = true")
    won_number = data["totalSize"]
    data = soql(context, "Select id from Opportunity where CloseDate = LAST_N_MONTHS:1")
    total_number = data["totalSize"]
    assert (str(math.trunc(won_number/total_number * 100))+"%" in driver.find_element(*home.win_rate_value).text)

    print("Days to Close")
    data = soql(context, "SELECT AVG(value__DaysToClose__c) FROM Opportunity WHERE CloseDate = LAST_N_MONTHS:1")
    assert_equals(locale.format_string("%d", dict(data["records"][0]).get("expr0"), grouping=True), driver.find_element(*home.days_close_value).text)

    print("sales rep")
    assert_equals(context.segment_info.get("users included"), driver.find_element(*home.sales_count_value).text)


