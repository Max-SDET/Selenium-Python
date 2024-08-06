import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class form_testing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com")

    def tearDown(self):
        self.driver.quit()

    def test_logo_size_check(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type ='submit']").click()
        time.sleep(2)

        # logo_element = driver.find_element(By.XPATH, "// img[@ alt = 'client brand banner']")
        logo_element = driver.find_element(By.CSS_SELECTOR,
                                           ".oxd-layout-navigation .oxd-sidepanel .oxd-navbar-nav .oxd-sidepanel-header .oxd-brand-banner > img")
        logo_size = logo_element.size

        # Checking Logo Size
        self.assertEqual(50, logo_size.get("height"))
        self.assertTrue(logo_size.get("width") == 182)
        self.assertDictEqual({'height': 50, 'width': 182}, logo_size)

        # Checkin alignment of elements on the page
        window_size = driver.get_window_size()
        logo_location = logo_element.location
        top_right_logo_corner_x_location = logo_size.get('width') + logo_location.get('x')
        self.assertTrue(top_right_logo_corner_x_location < (window_size.get('width') / 2))


if __name__ == '__main__':
    unittest.main()
