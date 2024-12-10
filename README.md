🧪 Movie Management Application - Pytest Automation Suite

🌟 Overview

    This project provides a robust Pytest automation suite for testing the Movie Management Application. The test suite ensures the application's stability, functionality, and security through comprehensive test scenarios.

🛠 Features

    - 20 Automated Test Cases:


        - Functional tests: Validate key features like user signup, login, and interactions.
        - Smoke tests: Verify essential workflows such as admin login and dashboard access.
        - Security tests: Check vulnerabilities like duplicate entries and unauthorized access.
        - Acceptance tests: Confirm the application meets user and business expectations.
    - Selenium WebDriver Integration: Automates user interactions on the web application.
    - HTML Reporting: Generates detailed test execution reports.
    - Fixtures for Reusability: Includes a setup fixture for streamlined test preparation.
  📂 Project Structure


      .
      ├── app.py                 # Main Flask application
      ├── movie.py               # Movie class and TMDb API integration
      ├── templates/             # HTML templates
      ├── static/                # Static assets
      ├── tests/                 # Pytest test suite
      │   ├── conftest.py        # Global fixtures
      │   ├── test_project.py    # Main test cases
      │   └── report.html        # HTML test report
      ├── requirements.txt       # Dependencies for the project
      ├── pytest.ini             # Pytest configuration file
      └── README.md              # Project documentation
  🔧 Setup Guide
  Prerequisites

      - Python 3.x installed.
      - Google Chrome browser and WebDriver (via webdriver-manager).
  Installation 
  1. Clone this repository:


    git clone https://github.com/matanohana433/movie-app-testing.git
    cd movie-app-testing
2. Create a virtual environment and activate it:

    Windows:


    python -m venv venv
    venv\Scripts\activate
macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate
3. Install dependencies:


    pip install -r requirements.txt
🚀 Running Tests


1. Run All Tests


    pytest --html=report.html --self-contained-html
2. Run Tests by Mark

  To execute specific categories:

  - Functional tests:

        pytest -m functional --html=report_functional.html --self-contained-html
  - Smoke tests:

        pytest -m smoke --html=report_smoke.html --self-contained-html
  - Security tests:

        pytest -m security --html=report_security.html --self-contained-html
  - Acceptance tests:
    
        pytest -m acceptance --html=report_acceptance.html --self-contained-html
🧪 Testing Categories


1. Functional Tests


    - Validate core application features, such as:
      - User signup and login.
      - Leaving comments on movies.
      - Logging out successfully.
2. Smoke Tests


    - Confirm critical workflows, such as:
      - Admin login.
      - Accessing the admin dashboard.
      - Managing users and comments.
3. Security Tests


    - Ensure application security by:
        - Preventing duplicate user creation.
        - Blocking unauthorized access to admin features.
        - Checking incorrect login attempts.
4. Acceptance Tests


    - Verify the application meets business requirements:
        - Adding new movies.
        - Ensuring data consistency across the dashboard and homepage.
📊 Example HTML Report


    - The test execution generates an HTML report (report.html), which includes:
        - Test results summary (e.g., passed, failed).
        - Test execution duration.
        - Detailed logs for each test case.
🌟 Key Features


Reusable Fixtures:

    conftest.py provides a global setup fixture for initializing WebDriver, selectors, and options.
Cross-Test Interaction:

    Tests validate changes across user actions, such as adding movies and checking updates on the admin dashboard.
Detailed Reporting:

    The HTML report (report.html) provides a clear view of test results, including success and failure logs.
🚀 Future Enhancements

    Extend browser compatibility with Firefox and Edge WebDrivers.
    Integrate with CI/CD pipelines (e.g., GitHub Actions, Jenkins).
    Enhance error handling for test failures.
    Add performance testing for application responsiveness.
📬 Contact
For questions or collaboration:

Email: matanohana433@gmail.com
GitHub: matanohana433
