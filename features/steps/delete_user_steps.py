from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('I delete the user "{username}"')
def step_delete_user(context, username):
    wait = WebDriverWait(context.driver, 10)
    delete_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f'//td[contains(text(), "{username}")]/following-sibling::td/button[@ng-click="delUser()"]')))
    delete_button.click()
    alert = wait.until(EC.alert_is_present())
    alert.accept()


@then('I should not see the user "{username}" in the table')
def step_verify_user_not_in_table(context, username):
    wait = WebDriverWait(context.driver, 10)
    wait.until(
        EC.invisibility_of_element_located((By.XPATH, f'//table//td[contains(text(), "{username}")]'))
    )
    context.driver.quit()
