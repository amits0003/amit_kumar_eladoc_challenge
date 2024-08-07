from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@when('I add a new user with the following details')
def step_add_user(context):
    wait = WebDriverWait(context.driver, 10)

    # Click the "Add User" button
    add_user_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ng-click="pop()"]')))
    add_user_button.click()

    # Fill out the form
    user_details = context.table.rows[0]
    wait.until(EC.element_to_be_clickable((By.NAME, 'FirstName'))).send_keys(user_details['First Name'])
    wait.until(EC.element_to_be_clickable((By.NAME, 'LastName'))).send_keys(user_details['Last Name'])
    wait.until(EC.element_to_be_clickable((By.NAME, 'UserName'))).send_keys(user_details['User Name'])
    wait.until(EC.element_to_be_clickable((By.NAME, 'Password'))).send_keys(user_details['Password'])

    # Select the customer
    customer_value = "(//label/input[@name='optionsRadios'])[1]" if user_details['Customer'] == 'Company AAA' else "(//label/input[@name='optionsRadios'])[2]"
    wait.until(EC.element_to_be_clickable((By.XPATH, f'{customer_value}'))).click()

    # Select the role
    role_select = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'RoleId'))))
    role_select.select_by_visible_text(user_details['Role'])

    wait.until(EC.element_to_be_clickable((By.NAME, 'Email'))).send_keys(user_details['E-mail'])
    wait.until(EC.element_to_be_clickable((By.NAME, 'Mobilephone'))).send_keys(user_details['Cell Phone'])

    # Click the "Save" button
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ng-click="save(user)"]'))).click()


@then('I should see the user "{full_name}" in the table')
def step_verify_user_in_table(context, full_name):
    wait = WebDriverWait(context.driver, 10)
    wait.until(
        EC.presence_of_element_located((By.XPATH, f'//table//td[text()="{full_name}"]'))
    )
    context.driver.quit()
