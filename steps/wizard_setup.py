# -*- coding: UTF-8 -*-
import time

import requests
from behave import step
from selenium.webdriver.common.by import By
from nose.tools import assert_equals, assert_in
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.setup_wizard_page import SetupWizardPage


@step("I start the setup of the assistant to add Sales Value app")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser

    # Todo: step according to the role
    print(context.current_role)

    # first step of the wizard validation
    wizard = SetupWizardPage(driver)
    assert_equals(parser.get('Setup Wizard', 'Title'), driver.find_element(*wizard.modal_title).text)
    assert_equals(parser.get('Setup Wizard', 'Next button'), driver.find_element(*wizard.modal_next_button).text)
    assert_equals(parser.get('Setup Wizard', 'Setup title'), driver.find_element(*wizard.modal_section_title).text)
    assert_equals(parser.get('Setup Wizard', 'Setup description'), driver.find_element(*wizard.setup_description).text)
    assert_equals(parser.get('Setup Wizard', 'Setup text'), driver.find_element(*wizard.setup_text).text)
    check_img(driver, *wizard.setup_img)
    wizard.verify_progress_bar(1)
    driver.find_element(*wizard.modal_next_button).click()


@step("in the legal step I try to advance and verify the condition according of readying links")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    # first step of the wizard validation
    wizard = SetupWizardPage(driver)
    wizard.verify_progress_bar(2)
    # second step of the wizard validation
    assert_equals(parser.get('Setup Wizard', 'Title'), driver.find_element(*wizard.modal_title).text)
    assert_equals(parser.get('Setup Wizard', 'Next button'), driver.find_element(*wizard.modal_next_button).text)
    assert_equals(parser.get('Setup Wizard', 'Previous button'),
                  driver.find_element(*wizard.modal_previous_button).text)
    assert_equals(parser.get('Setup Wizard', 'Legal title'), driver.find_element(*wizard.modal_section_title).text)
    assert_equals(parser.get('Setup Wizard', 'Legal text'), driver.find_element(*wizard.legal_text).text)
    assert_equals(parser.get('Setup Wizard', 'Legal condition'), driver.find_element(*wizard.legal_condition).text)

    for line in context.table:
        link = line["link"]
        behavior = line["expected behavior"]

        if link == "none":
            # scenario of trying to advance without reading any document just clicking next
            driver.find_element(*wizard.modal_next_button).click()

        elif link == "Sales Value App Exhibits":
            # scenario of trying to advance reading just 1 document and clicking the checkbox
            driver.find_element(By.LINK_TEXT, parser.get('Setup Wizard', 'Legal sales link')).click()
            wizard.check_doc_link("sales")

            # add this due a different behavior between firefox and chrome
            if len(driver.find_elements(*wizard.legal_checkbox)) > 0:
                driver.find_element(*wizard.legal_checkbox).click()
            else:
                wizard.wait_for_frame_and_switch(10)
                driver.find_element(*wizard.legal_checkbox).click()

        elif link == "Unified Pilot Research Agreement":
            # scenario of trying to advance reading just 1 document and clicking the checkbox
            driver.find_element(By.LINK_TEXT, parser.get('Setup Wizard', 'Legal pilot link')).click()
            wizard.check_doc_link("opt in")

            # add this due a different behavior between firefox and chrome
            if len(driver.find_elements(*wizard.legal_checkbox)) > 0:
                driver.find_element(*wizard.legal_checkbox).click()
            else:
                wizard.wait_for_frame_and_switch(10)
                driver.find_element(*wizard.legal_checkbox).click()

        else:
            # scenario of trying to advance reading all the documents and clicking the checkbox and next
            driver.find_element(By.LINK_TEXT, parser.get('Setup Wizard', 'Legal sales link')).click()
            wizard.check_doc_link("sales")
            # add this due a different behavior between firefox and chrome
            if len(driver.find_elements(By.LINK_TEXT, parser.get('Setup Wizard', 'Legal pilot link'))) > 0:
                driver.find_element(By.LINK_TEXT, parser.get('Setup Wizard', 'Legal pilot link')).click()
            else:
                wizard.wait_for_frame_and_switch(10)
                driver.find_element(By.LINK_TEXT, parser.get('Setup Wizard', 'Legal pilot link')).click()
            wizard.check_doc_link("opt in")

            # add this due a different behavior between firefox and chrome
            if len(driver.find_elements(*wizard.legal_checkbox)) > 0:
                driver.find_element(*wizard.legal_checkbox).click()
            else:
                wizard.wait_for_frame_and_switch(10)
                driver.find_element(*wizard.legal_checkbox).click()
            driver.find_element(*wizard.modal_next_button).click()

        if behavior == "you must read and agree the conditions validation":
            warning = wizard.get_list_warnings()
            assert_in(parser.get('Setup Wizard', 'Legal warning-2'), warning)
        elif behavior == "Open and read both agreements.":
            warning = wizard.get_list_warnings()
            assert_in(parser.get('Setup Wizard', 'Legal warning-1'), warning)


@step(u'in the benchmark step I just press next, "{text}" checking and reading the agreement')
def step_impl(context, text):
    """
    :param text: options with and without
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    wizard = SetupWizardPage(driver)
    wizard.verify_progress_bar(3)
    # third step of the wizard validation
    assert_equals(parser.get('Setup Wizard', 'Title'),
                  driver.find_element(*wizard.modal_title).text)
    assert_equals(parser.get('Setup Wizard', 'Next button'), driver.find_element(*wizard.modal_next_button).text)
    assert_equals(parser.get('Setup Wizard', 'Previous button'),
                  driver.find_element(*wizard.modal_previous_button).text)
    assert_equals(parser.get('Setup Wizard', 'Benchmark title'), driver.find_element(*wizard.modal_section_title).text)
    assert_equals(parser.get('Setup Wizard', 'Benchmark description'),
                  driver.find_element(*wizard.benchmark_description).text)
    assert_equals(parser.get('Setup Wizard', 'Benchmark text'), driver.find_element(*wizard.benchmark_text).text)
    assert_equals(parser.get('Setup Wizard', 'Benchmark condition'),
                  driver.find_element(*wizard.benchmark_condition).text)

    if text == "with":
        print("we are going to check only if the document opens and url is right")
        driver.find_element(By.LINK_TEXT, parser.get('Setup Wizard', 'Benchmark link')).click()
        wizard.check_doc_link("benchmark")
        driver.find_element(*wizard.benchmark_checkbox).click()
        driver.find_element(*wizard.modal_next_button).click()

    else:
        driver.find_element(*wizard.modal_next_button).click()

@step("I finish the last step of the setup wizard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = context.driver
    parser = context.parser
    # first step of the wizard validation
    wizard = SetupWizardPage(driver)
    wizard.verify_progress_bar(4)
    # fourth step of the wizard validation
    assert_equals(parser.get('Setup Wizard', 'Title'), driver.find_element(*wizard.modal_title).text)
    assert_equals(parser.get('Setup Wizard', 'Lets Go button'), driver.find_element(*wizard.modal_next_button).text)
    assert_equals(parser.get('Setup Wizard', 'You are done title'), driver.find_element(*wizard.you_done_title).text)
    assert_equals(parser.get('Setup Wizard', 'You are done description'),
                  driver.find_element(*wizard.you_done_description).text)
    check_img(driver, *wizard.you_done_img)
    # wizard.modal_next_button.click()


def check_img(driver, by, locator):
    """assert img resource is loading"""
    img_link = driver.find_element(by, locator).get_attribute("src")
    r = requests.get(img_link)
    assert_equals(r.status_code, 200)
