import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


class form_testing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.empID = randint(7000, 90000)

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type ='submit']").click()

        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//header//h6")))
        text = driver.find_element(By.XPATH, "//header//h6").text
        assert text == "Dashboard"

        # click PIM button
        driver.find_element(By.XPATH, "//a[contains(@href, '/web/index.php/pim/viewPimModule')]").click()
        time.sleep(2)
        # click Add
        driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
        time.sleep(2)

        # click And clear and add value  employee id
        driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").clear()
        driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(str(self.empID))

        # click first name
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Chris")
        # click Last name
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Smith")

        # click save
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        # click Employee list
        driver.find_element(By.XPATH, "//a[contains(text(),'Employee List')]").click()
        time.sleep(3)
        # click  search by name
        driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys("Chris Smith")
        # click search
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(3)

        # Expected correct name
        first_name = driver.find_element(By.XPATH, "//div[contains(text(),'Chris')]").text
        time.sleep(1)
        last_name = driver.find_element(By.XPATH, "//div[contains(text(),'Smith')]").text

        self.assertEqual("Chris", first_name)
        self.assertEqual("Smith", last_name)

        if __name__ == "__main__":
            unittest.main()
