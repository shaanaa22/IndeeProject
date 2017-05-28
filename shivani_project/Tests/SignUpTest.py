import unittest

from selenium import webdriver

class MyIndeeTest(unittest.TestCase):

    @classmethod
    def setUp(cls):

        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_signup(self):


        self.driver.get("https://www.indee.tv")
        self.driver.get_screenshot_as_file("../Screenshots/%homepage.png")
        sign_up = self.driver.find_element_by_link_text('SIGN UP')
        sign_up.click()

        email = self.driver.find_element_by_xpath("//input[@placeholder='Email']")
        email.send_keys("sandhfj@sdvfnjhm")

        password = self.driver.find_element_by_xpath("//input[@placeholder='Password']")
        password.send_keys("asdferd")

        confirm_password = self.driver.find_element_by_xpath("//input[@placeholder='Confirm Password']")
        confirm_password.send_keys("asdferd")

        first_name = self.driver.find_element_by_xpath("//input[@placeholder='First Name']")
        first_name.send_keys("Shivani")

        last_name = self.driver.find_element_by_xpath("//input[@placeholder='Last Name']")
        last_name.send_keys("Thakur")

        company_name = self.driver.find_element_by_xpath("//input[@placeholder='Company Name (Optional)']")
        company_name.send_keys("Indee")

        checkbox_ = self.driver.find_element_by_xpath("//input[@type='checkbox']")
        checkbox_.click()

        self.driver.get_screenshot_as_file("../Screenshots/%signuppage_before.png")

        sign_up_submit = self.driver.find_element_by_xpath("//button[@type='submit']")
        sign_up_submit.click()

        self.driver.get_screenshot_as_file("../Screenshots/%signuppage_after.png")

        try:
            welcome_msg = self.driver.find_element_by_xpath("//*[contains(text, 'WELCOME TO INDEE')]")

            msg_check = welcome_msg.is_displayed()

            if (msg_check):
                print "Sign up success"

        except Exception:
            print "Sign up Failure"

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
