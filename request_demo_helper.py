from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def go_to_homepage(self):
        driver = self.driver
        driver.get("https://www.dealerscience.com/site/")

    def click_request_demo(self):
        driver = self.driver
        driver.find_element_by_id("menu-item-431").click()

    def click_submit(self):
        driver = self.driver
        driver.find_element_by_css_selector("button.btn").click()

    def enter_message(self, message):
        driver = self.driver
        driver.find_element_by_name("message").clear()
        driver.find_element_by_name("message").send_keys("%s" % message)

    def enter_dealership(self, dealership):
        driver = self.driver
        driver.find_element_by_name("dealership").clear()
        driver.find_element_by_name("dealership").send_keys("%s" % dealership)

    def enter_email(self, email):
        driver = self.driver
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("%s" % email)

    def enter_phone(self, phone):
        driver = self.driver
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("%s" % phone)

    def enter_name(self, name):
        driver = self.driver
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("%s" % name)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def destroy(self):
        self.driver.quit()
