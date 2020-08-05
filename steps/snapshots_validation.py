
import time
from utils.salesforce import soql
from behave import step, then
from nose.tools import assert_equals
from selenium.webdriver.common.by import By
from pages.tabs_bar import TabsBar
from pages.snapshots_page import SnapshotsPage
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale

@step(u'I navigate to the snapshot repository, looking in the filter for "{text}"')
def step_impl(context, text):
    """
    :param text: get recently used or all in snapshots filter
    :type context: behave.runner.Context
    """
    driver = context.driver
    tab_bar = TabsBar(driver)
    tab_bar.wait_for_bar(30)
    tab_bar.navigate_to("snapshots")
    snap = SnapshotsPage(driver)
    snap.select_mode(text)
    time.sleep(3)


@step("I verify that the snapshots have been created correctly")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    snap = SnapshotsPage(driver)
    context.segment_info = {'name': 'Automation 20200803180012'}
    name = context.segment_info.get("name")

    year = name[11:15]
    month = name[15:17]
    day = name[17:19]
    hour = name[19:21]
    min = name[21:23]
    am_pm = "AM"

    if int(hour) > 12:
        am_pm = "PM"
        hour = str(int(hour)-12)
    date = str(int(month))+"/"+str(int(day))+"/"+str(int(year))+", "+str(int(hour))+":"+min+" "+am_pm

    snap.sort_snapshots()
    assert_equals(parser.get('Snapshots', 'Table header1'), driver.find_element(*snap.snapshots_name_header).text)
    assert_equals(parser.get('Snapshots', 'Table header2'), driver.find_element(*snap.create_date_header).text)
    assert_equals(parser.get('Snapshots', 'Table header3'), driver.find_element(*snap.snapshots_header).text)
    assert_equals(parser.get('Snapshots', 'Table header4'), driver.find_element(*snap.historical_header).text)
    assert_equals(parser.get('Snapshots', 'Table header5'), driver.find_element(*snap.snapshots_date_header).text)

    rows = snap.get_table_rows(name)
    print("========")
    len(rows)

    print(rows)
    print("========")
    # verify 13 snapshots are present with the desired header name
    assert len(rows) == 13
    # verify snapshots dates
    end_month = 1
    initial_date = str(int(month))+"/"+str(int(day))+"/"+str(int(year))
    for element in rows:
        # assert_equals(date, element.get("created_date"))
        snap_date = element.get("snapshot_date")
        now = datetime.strptime(initial_date, '%m/%d/%Y')
        expected_date = (now + relativedelta(day=1, months=(-14+end_month))).strftime("%-m/%-d/%Y")
        assert_equals(str(expected_date),snap_date)
        end_month = end_month + 1


@step("I wait 10 min or until the snapshotobject is created")
def step_impl(context):
    """
    step created to wait as long as necesary to snapshot object to be created
    probably have a timeout because can be waiting forever
    :type context: behave.runner.Context
    """
    max_time = 600
    waiting = True
    round = 0
    name = context.segment_info.get("name")
    query = "select insightStatus__c from snapshot__c where snapshotHeader__c = '{name}'"
    print(query)
    while waiting:
        print("starting to wait sec "+str(round))
        round = round + 60
        #data = soql(context, query)
        #print(data)
        #total_segments = locale.format_string("%d", data['totalSize'], grouping=True)
        #print(total_segments)
        time.sleep(60)
        if round == max_time:
            print("max timeout reach")
            waiting = False


@then("I verify that the latest snapshot have the right KPI values")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    snap = SnapshotsPage(driver)
    context.segment_info = {'name': 'Automation 20200803180012', 'industry': 'Banking'}
    name = context.segment_info.get("name")
    peer = context.segment_info.get("industry")

    year = name[11:15]
    month = name[15:17]
    day = name[17:19]
    hour = name[19:21]
    min = name[21:23]
    am_pm = "AM"

    if int(hour) > 12:
        am_pm = "PM"
        hour = str(int(hour)-12)
    initial_date = str(int(month))+"/"+str(int(day))+"/"+str(int(year))
    now = datetime.strptime(initial_date, '%m/%d/%Y')
    expected_date = (now + relativedelta(day=1, months=(-1))).strftime("%-m/%-d/%Y")

    snap.sort_snapshots()
    assert_equals(parser.get('Snapshots', 'Table header1'), driver.find_element(*snap.snapshots_name_header).text)
    assert_equals(parser.get('Snapshots', 'Table header2'), driver.find_element(*snap.create_date_header).text)
    assert_equals(parser.get('Snapshots', 'Table header3'), driver.find_element(*snap.snapshots_header).text)
    assert_equals(parser.get('Snapshots', 'Table header4'), driver.find_element(*snap.historical_header).text)
    assert_equals(parser.get('Snapshots', 'Table header5'), driver.find_element(*snap.snapshots_date_header).text)

    snap.enter_snapshot(name, expected_date)
    assert_equals(parser.get('Snapshots', 'Peer Group'), driver.find_element(*snap.peer_group_label).text)
    assert_equals(peer, driver.find_element(*snap.peer_group_value).text)
    assert_equals(parser.get('Snapshots', 'Snapshot Header label'), driver.find_element(*snap.snapshots_header_label).text)
    assert_equals(parser.get('Snapshots', 'Won Opportunities'), driver.find_element(*snap.won_opp_label).text)
    data = soql(context, "Select count() from Opportunity where CloseDate = LAST_N_MONTHS:1 and IsWon = true")
    assert_equals(locale.format_string("%f", data['totalSize'], grouping=True), driver.find_element(*snap.won_opp_value).text)
    assert_equals(parser.get('Snapshots', 'Average Sales Size'), driver.find_element(*snap.average_sales_size_label).text)
    assert_equals(parser.get('Snapshots', 'Closed Opportunities'), driver.find_element(*snap.closed_opportunities_label).text)
    assert_equals(parser.get('Snapshots', 'Win Rate'), driver.find_element(*snap.win_rate_label).text)
    assert_equals(parser.get('Snapshots', 'Sales Per Rep'), driver.find_element(*snap.sales_per_rep_label).text)
    assert_equals(parser.get('Snapshots', 'Lead Volume'), driver.find_element(*snap.lead_volume_label).text)

