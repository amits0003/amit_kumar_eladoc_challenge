from behave import given
from selenium import webdriver


@given('I open the webtable application')
def step_open_webtable(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://www.way2automation.com/angularjs-protractor/webtables/')
