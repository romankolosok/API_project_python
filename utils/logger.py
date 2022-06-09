import datetime
import os
from requests import Response

"""class for creating test logs"""
class Log_creator():

    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, "a", encoding="utf-8") as log_file:
            log_file.write(data)


    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get("PYTEST_CURRENT_TEST")

        data_tool_add = f"\n--------------\n"
        data_tool_add += f"Test: {test_name}\n"
        data_tool_add += f"Time: {str(datetime.datetime.now())}\n"
        data_tool_add += f"Request Method: {method}\n"
        data_tool_add += f"Request URL: {url}\n\n"

        cls.write_log_to_file(data_tool_add)


    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_tool_add = f"Response code: {str(result.status_code)}\n"
        data_tool_add += f"Response text: {result.text}\n"
        data_tool_add += f"Response headers: {headers_as_dict}\n"
        data_tool_add += f"Response cookies: {cookies_as_dict}\n"
        data_tool_add += f"\n--------------\n"

        cls.write_log_to_file(data_tool_add)










