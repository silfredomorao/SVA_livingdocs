# -*- coding: UTF-8 -*-
import locale
import time
from datetime import datetime

import dateutil
from behave import step, then
from nose.tools import assert_equals
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.segments_creation_page import SegmentsCreationPage
from utils.salesforce import soql


@step(u'I try to create a new segment with name: "{name}"')
def step_impl(context, name):
    """
    :param text: options with and without
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    home = HomePage(driver)
    home.wait_for_new_segment_button(15)

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

    driver.find_element(*home.new_segment).click()

    if name == " ":
        name = ""
    elif name == "SqID":
        name = "Automation " + (str(datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', ''))[0:14]
    context.segment_info = {"name":name}
    print("############################################")
    print(context.segment_info)
    print("############################################")

    segment_wizard = SegmentsCreationPage(driver)
    assert_equals(parser.get('New Segment', 'Title'), driver.find_element(*segment_wizard.modal_title).text)
    assert_equals(parser.get('New Segment', 'Next button'), driver.find_element(*segment_wizard.modal_next_button).text)
    assert_equals(parser.get('New Segment', 'Information title'),
                  driver.find_element(*segment_wizard.modal_section_title).text)
    assert_equals(parser.get('New Segment', 'Information description'),
                  driver.find_element(*segment_wizard.information_segment_description).text)
    assert_equals(parser.get('New Segment', 'Information text'),
                  driver.find_element(*segment_wizard.information_segment_text).text)
    assert_equals(parser.get('New Segment', 'Information text2'),
                  driver.find_element(*segment_wizard.information_segment_text2).text)
    assert_equals(parser.get('New Segment', 'Information label'),
                  driver.find_element(*segment_wizard.information_segment_required_label).text)
    segment_wizard.verify_progress_bar(1)

    driver.find_element(*segment_wizard.information_segment_input).send_keys(name)
    driver.find_element(*segment_wizard.modal_next_button).click()
    time.sleep(4)


@then(u'the warning that "{warning}" field is required is shown preventing continuing')
def step_impl(context, warning):
    """
    :param warning:
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    segment_wizard = SegmentsCreationPage(driver)
    if warning == "segment name":
        assert_equals(parser.get('New Segment', 'Information warning'),
                      driver.find_element(*segment_wizard.information_segment_warning).text)
    elif warning == "peer name":
        assert_equals(parser.get('New Segment', 'Peers warning'),
                      driver.find_element(*segment_wizard.peer_warning).text)
    else:
        print("warming type is not present")


@then("the verify the new segments example link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    segment_wizard = SegmentsCreationPage(driver)
    driver.find_element(By.LINK_TEXT, parser.get('New Segment', 'Segment example link')).click()
    segment_wizard.verify_progress_bar(2)
    segment_wizard.check_doc_link("segment example")




@step("I create a new Opportunity filter setup according this table")
def step_impl(context):
    """
    :param Amount, Field, Operator, Value (s), Continue next screen
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    locale.setlocale(locale.LC_ALL, 'en_US')
    segment_wizard = SegmentsCreationPage(driver)
    segment_wizard.wait_for_title(10)
    data = soql(context, "Select Id from Opportunity where CloseDate = LAST_N_MONTHS:13 and IsClosed = true")
    total_segments = locale.format_string("%d", data['totalSize'], grouping=True)
    assert_equals(parser.get('New Segment', 'Next button'), driver.find_element(*segment_wizard.modal_next_button).text)
    assert_equals(parser.get('New Segment', 'Title'), driver.find_element(*segment_wizard.modal_title).text)
    assert_equals(parser.get('New Segment', 'Previous button'),
                  driver.find_element(*segment_wizard.modal_previous_button).text)
    segment_wizard.verify_progress_bar(2)
    assert_equals(parser.get('New Segment', 'Opportunity description'),
                  driver.find_element(*segment_wizard.opportunity_description).text)
    assert_equals(parser.get('New Segment', 'Opportunity text'),
                  driver.find_element(*segment_wizard.opportunity_text).text)
    assert_equals(parser.get('New Segment', 'Opportunity description2').replace('\r', '').replace('\n', ''),
                  driver.find_element(*segment_wizard.opportunity_description_filter).text.replace('\r', '').replace(
                      '\n', ''))
    assert_equals(parser.get('New Segment', 'Opportunity text3').replace('\r', '').replace('\n', ''),
                  driver.find_element(*segment_wizard.opportunity_text_filter).text.replace('\r', '').replace('\n', ''))
    assert_equals(parser.get('New Segment', 'Opportunity closed') + " " + context.segment_info["name"] + ": " + total_segments, driver.find_element(*segment_wizard.opportunity_total).text)
    assert_equals(parser.get('New Segment', 'Opportunity track amount'),
                  driver.find_element(*segment_wizard.opportunity_label_amount).get_attribute('value'))

    segment_wizard.add_filter_fieldset(str(context.table))

    row_number = 1

    for line in context.table:
        amount = line["Amount"]
        field = line["Field"]
        operator = line["Operator"]
        value = line["Value"]
        continue_next = line["Continue"]
        segment_wizard.select_amount_type(amount)
        element = driver.find_element(*segment_wizard.opportunity_label_amount)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        assert_equals(parser.get('New Segment', 'Opportunity Value Label'),
                      driver.find_element(*segment_wizard.opportunity_values_label).text)
        assert_equals(parser.get('New Segment', 'Opportunity Field Label'),
                      driver.find_element(*segment_wizard.opportunity_field_label).text)
        assert_equals(parser.get('New Segment', 'Opportunity Operator Label'),
                      driver.find_element(*segment_wizard.opportunity_operator_label).text)
        assert_equals(parser.get('New Segment', 'Opportunity field placeholder'),
                      driver.find_element(*segment_wizard.opportunity_field_input).get_attribute("placeholder"))
        assert_equals(parser.get('New Segment', 'Opportunity Operator placeholder'),
                      driver.find_element(*segment_wizard.opportunity_operator_input).get_attribute("placeholder"))

        segment_wizard.fill_opportunity_filter(row_number, field, operator, value)

        row_number = row_number + 1

        if continue_next == "yes":
            time.sleep(15)
            # TODO: replace for proper wait when we have a proper query
            context.segment_info["closed opportunities"] = driver.find_element(
                *segment_wizard.opportunity_closed_included).text
            driver.find_element(*segment_wizard.modal_next_button).click()


@step("I create a new Sales filter setup according this table")
def step_impl(context):
    """
    :param Field, Operator, Value (s), Continue next screen
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    segment_wizard = SegmentsCreationPage(driver)
    segment_wizard.wait_for_title(10)

    assert_equals(parser.get('New Segment', 'Previous button'),
                  driver.find_element(*segment_wizard.modal_previous_button).text)
    assert_equals(parser.get('New Segment', 'Next button'), driver.find_element(*segment_wizard.modal_next_button).text)
    assert_equals(parser.get('New Segment', 'Title'), driver.find_element(*segment_wizard.modal_title).text)


    assert_equals(parser.get('New Segment', 'Sales text'),
                  driver.find_element(*segment_wizard.sales_text).text)
    assert_equals(parser.get('New Segment', 'Sales text2'),
                  driver.find_element(*segment_wizard.sales_text2).text)
    assert_equals(parser.get('New Segment', 'Sales text3'),
                  driver.find_element(*segment_wizard.sales_text3).text)
    assert_equals(parser.get('New Segment', 'Sales description'),
                  driver.find_element(*segment_wizard.sales_description).text)
    assert_equals(parser.get('New Segment', 'Add Filter'),
                  driver.find_element(*segment_wizard.sales_add_filter).text)
    assert parser.get('New Segment', 'Sales total') + " " + context.segment_info.get("name") in driver.find_element(
        *segment_wizard.sales_user_total).text
    segment_wizard.verify_progress_bar(3)

    segment_wizard.add_filter_fieldset(str(context.table))
    row_number = 1

    for line in context.table:
        field = line["Field"]
        operator = line["Operator"]
        value = line["Value"]
        continue_next = line["Continue"]
        # Todo regular assertion on the labels of the grid pending...  probably the opportunity filter can work here
        segment_wizard.fill_opportunity_filter(row_number, field, operator, value)
        row_number = row_number + 1

        if continue_next == "yes":
            # TODO: find the proper pause at this point
            time.sleep(15)
            context.segment_info["users included"] = driver.find_element(
                *segment_wizard.opportunity_users_included).text
            driver.find_element(*segment_wizard.modal_next_button).click()
            time.sleep(3)


@then(u'I select the peer group filter "{peers}"')
def step_impl(context, peers):
    """
    :param peers:
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    segment_wizard = SegmentsCreationPage(driver)
    segment_wizard.wait_for_title(10)
    segment_wizard.verify_progress_bar(4)
    assert_equals(parser.get('New Segment', 'Done button'), driver.find_element(*segment_wizard.modal_next_button).text)
    assert_equals(parser.get('New Segment', 'Previous button'),
                  driver.find_element(*segment_wizard.modal_previous_button).text)
    assert_equals(parser.get('New Segment', 'Title'), driver.find_element(*segment_wizard.modal_title).text)
    assert_equals(parser.get('New Segment', 'Peers description'),
                  driver.find_element(*segment_wizard.peers_description).text)
    assert_equals(parser.get('New Segment', 'Peers text'),
                  driver.find_element(*segment_wizard.peers_text).text)
    assert_equals(parser.get('New Segment', 'Peers text2'),
                  driver.find_element(*segment_wizard.peers_text2).text)
    assert_equals(parser.get('New Segment', 'Peers placeholder'),
                  driver.find_element(*segment_wizard.peers_selector).get_attribute("placeholder"))
    if peers == " ":
        peers = ""
    segment_wizard.select_peer(peers)
    context.segment_info["industry"] = peers
    driver.find_element(*segment_wizard.modal_next_button).click()
    time.sleep(10)


@step(u'I delete the filter number')
def step_impl(context):
    """
    :param number: number of field set to delete
    :type context: behave.runner.Context
    """
    driver = context.driver
    segment_wizard = SegmentsCreationPage(driver)
    segment_wizard.wait_for_title(10)
    print("entro en delete")
    for line in context.table:
        number = line["Number"]
        continue_next = line["Continue"]
        segment_wizard.delete_opportunity_filter(number)
        if continue_next == "yes":
            time.sleep(4)
            # TODO: replace for proper wait when we have a proper query
            driver.find_element(*segment_wizard.modal_next_button).click()


@then("I Edit the filter number:")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = context.driver
    segment_wizard = SegmentsCreationPage(driver)
    segment_wizard.wait_for_title(10)

    for line in context.table:
        number = line["Number"]
        field = line["Field"]
        operator = line["Operator"]
        value = line["Value"]
        continue_next = line["Continue"]
        segment_wizard.fill_opportunity_filter(number, field, operator, value)
        if continue_next == "yes":
            time.sleep(15)
            # TODO: replace for proper wait when we have a proper query
            driver.find_element(*segment_wizard.modal_next_button).click()


@then(u'I cant advance and "{warning}" msg is present')
def step_impl(context, warning):
    """
    :param warning: warning key from language file
    :type context: behave.runner.Context
    """
    parser = context.parser
    driver = context.driver
    segment_wizard = SegmentsCreationPage(driver)
    segment_wizard.wait_for_title(10)
    assert_equals(parser.get('New Segment', warning),
                  driver.find_element(*segment_wizard.opportunity_warning).text)




