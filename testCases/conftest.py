from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    options = Options()
    options.add_argument("--disable-notifications")
    s = Service(executable_path="C:\\selenium browser drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    return driver


def pytest_configure(config):
    config._metadata['Project Name'] = 'Salesforce'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Zaloom'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

    #html report:pytest -s -v -n=3 --html=Reports\report.html
