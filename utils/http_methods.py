import allure
import requests

from utils.logger import Log_creator

"""List of HTTP-methods"""
class Http_method():
    headers = {'Content-Type' : 'application/json'}
    cookie = ""

    """Custom request analogs"""
    @staticmethod
    def get(url):
        with allure.step("GET"):
            Log_creator.add_request(url, method="GET")
            result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
            Log_creator.add_response(result)
            return result

    @staticmethod
    def post(url,body):
        with allure.step("POST"):
            Log_creator.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Log_creator.add_response(result)
            return result

    @staticmethod
    def put(url,body):
        with allure.step("PUT"):
            Log_creator.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Log_creator.add_response(result)
            return result

    @staticmethod
    def delete(url,body):
        with allure.step("DELETE"):
            Log_creator.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
            Log_creator.add_response(result)
            return result