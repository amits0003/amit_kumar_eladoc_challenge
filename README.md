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

| amit_kumar_teledoc_challenge
    -|- features
        -|- steps
            -|- add_user_steps.py
            -|- common_steps.py
            -|- delete_user_steps.py
        -|- add_user.feature
        -|- delete_user.feature
        -|- environment.py
    -|- requirements.txt
    -|- venv
- **amit_kumar_teledoc_challenge ** Root repo containing all codes, env files and venv
- **features/**: Contains all the feature files and step definitions.
  - **steps/**: Contains Python files with step definitions.
    - `add_user_steps.py`: Step definitions for adding a user.
    - `common_steps.py`: Common step definitions shared across feature files.
    - `delete_user_steps.py`: Step definitions for deleting a user.
  - `add_user.feature`: Feature file for adding a user.
  - `delete_user.feature`: Feature file for deleting a user.
- **environment.py**: Contains environment-specific settings or hooks.
- **requirements.txt**: Lists the required Python packages for the project.
- **venv/**: Virtual environment directory.








