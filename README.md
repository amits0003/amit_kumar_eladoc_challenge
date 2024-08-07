# Webtables Automation

This project automates the webtable application available at http://www.way2automation.com/angularjs-protractor/webtables/ using Python, Selenium, and Behave (BDD framework).

## Installation

1. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Tests

1. Make sure you have ChromeDriver installed and it is in your PATH.

2. Run the tests:

    ```bash
    behave
    ```

## Features

- `add_user.feature`: Adds a user and validates the user has been added to the table.
- `delete_user.feature`: Deletes the user "novak" and validates the user has been deleted from the table.

## Project Structure

