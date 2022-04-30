from email import header
import re
from venv import create
import requests
import os
TOKEN = os.getenv('YD_TOKEN')

class YandexAPI():

    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'OAuth {self.token}'
        }
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'


    def create_folder(self, path='/folder'):
        params ={
            'path': path,
        }
        response = requests.put(url=self.url, params=params, headers=self.headers)
        return response


    def delete_folder(self, path='/folder'):
        params ={
            'path': path,
        }
        response = requests.delete(url=self.url, params=params, headers=self.headers)
        return response


    def get_info(self, path='/folder'):
        params ={
            'path': path,
        }
        response = requests.delete(url=self.url, params=params, headers=self.headers)
        return response

yandex_client = YandexAPI(TOKEN)
r = yandex_client.get_info(path='/netology')
print(r)