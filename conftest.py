from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="class")
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver. \
        Chrome(service=ChromeService(ChromeDriverManager(). \
                                     install()), options=chrome_options)
    return driver, By, Select
