import unittest
import os 
import sys
sys.path.append('..')
from login_yandex import login_yandex


LOGIN = os.getenv('YA_LOGIN')
PASSWORD = os.getenv('YA_PASSWORD')

class TestSelenimLogin(unittest.TestCase):
    
    def test_correct_log_pass(self):
        self.assertEqual(login_yandex(login=LOGIN, password=PASSWORD).current_url, 'https://passport.yandex.ru/profile')

    def test_incorrect_log_pass(self):
        self.assertEqual(login_yandex(login='qwerty', password='qwerty').current_url, 'https://passport.yandex.ru/auth/welcome')


if __name__ == '__main__':
    unittest.main()
