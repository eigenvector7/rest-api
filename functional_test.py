# Functional Test for Django powered rest APIs
# credit book titled: "Test driven development with Python"
# credit book author: Percival
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Iva was introduced to a new task management webapp by her colleague.
        # She goes to the homepage of the webapp
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mentiones "List Life"
        self.assertIn('To-Do List', self.browser.title)
        self.fail('Finish The Test!!!')
        # She is invited to enter her tasks in list life right away

        # She enters "Buy Plants for living room" and presses enter

        # The web app now shows her task in a numbered list:
        # 1. Buy plants for living room

        # The webapp still has another test box for her to enter yet another
        # item.
        # She enters: 2. Water the plants

        # The page updates and shows two items in her list now

        # Iva notices the message at the top of her list showing a unique URL
        # that she can use to return to her saved list.

        # She enters the URL in another browser and voila!! She can see the
        # saved list with another prompot to enter the text

        # Satisfied, she closes the browser window

if __name__ == '__main__':
    unittest.main(warnings='ignore')
