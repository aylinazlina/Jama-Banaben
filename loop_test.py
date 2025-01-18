import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize("username,password", [
    ("test", "test"),
    ("redwan", "1234"),
    ("siyam", "SiyamMia111"),
    ("Aylin", "2020")
])
def test_none_loop_login(driver, username, password):
    driver.get("http://127.0.0.1:8000/login/?next=/")
    username_field = driver.find_element(By.ID, "username")
    passw = driver.find_element(By.ID, "pass")  # Update if the ID is incorrect
    submit = driver.find_element(By.XPATH, "//input[@value='Login']")

    username_field.send_keys(username)
    passw.send_keys(password)
    submit.click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    print("Attempting login with:", username, password)
    print("Current URL:", driver.current_url)
    print("Page Source:", driver.page_source[:500])  # Debug page source

    # Update the success condition if necessary
    assert "Successful" in driver.page_source
