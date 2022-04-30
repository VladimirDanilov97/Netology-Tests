import unittest
import sys
sys.path.append('..')
from yandex import YandexAPI, TOKEN
from datetime import datetime
import time


class TestYandexAPI(unittest.TestCase):

    now = datetime.now().strftime('%d_%m_%y %H_%M_%S')
    yandex_client = YandexAPI(TOKEN)
    yandex_client_wrong_token = YandexAPI(token='*')

    def test_create_new_folder(self):
        
        self.assertEqual(
            self.yandex_client.create_folder(path='/'+self.now).status_code,
            201)
        
        self.assertEqual(
            self.yandex_client.get_info(path='/'+self.now).status_code,
            202)



        # Create existing folder
        self.assertEqual(
            self.yandex_client.create_folder(path='/'+self.now).status_code,
            409) 
       
        self.yandex_client.delete_folder(path='/'+self.now)
    

    def test_create_new_folder_wrong_token(self):
        self.assertEqual(
            self.yandex_client_wrong_token.create_folder(path='/'+self.now).status_code,
            401)
    

    def test_create_new_folder_wrong_path(self):
        self.assertEqual(
            self.yandex_client.create_folder(path='/new_folder/new_folder').status_code,
            409)
    
    
if __name__ == '__main__':
    unittest.main()