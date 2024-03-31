import requests
from allure import step
import json
from config import Env


# Изначально планировалось решать задачу полностью через api бэка, но сделал вывод, что это невыгодно из-за
# огромного количества фоновых запросов. Не скажу, что невозможно, просто неудобно.


def env():
    return Env


class ApiClient:
    # def __init__(self):
    #     self.base_url = env().host

    @step('Отправка GET-Запроса серверу')
    def get(self, url='/', params=None, headers=None):
        return requests.get(url, params=params, headers=headers)

    @step('Отправка POST-Запроса серверу')
    def post(self, url='/', data=None, headers=None, files=None):
        return requests.post(url, data=data, json=json, headers=headers, files=files)

    @step('Отправка PUT-Запроса серверу')
    def put(self, url='/', data=None, headers=None):
        return requests.put(url, data=data, json=json, headers=headers)

    @step('Отправка DELETE-Запроса серверу')
    def delete(self, url='/', headers=None):
        return requests.delete(url, headers=headers)
