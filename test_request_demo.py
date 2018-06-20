import time
import unittest

from request_demo_helper import Application


class DealerScience(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_dealer(self):
        self.app.go_to_homepage()
        self.app.click_request_demo()
        self.app.enter_name("Tester")
        self.app.enter_phone("1234567890")
        self.app.enter_email("tester@fake.com")
        self.app.enter_dealership("Honda Waltham")
        self.app.enter_message("testing request")
        self.app.click_submit()
        time.sleep(10)
        self.assertEqual("Thank you for contacting us! We will get back to you shortly. Have a great day!",
                         self.app.close_alert_and_get_its_text())

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()