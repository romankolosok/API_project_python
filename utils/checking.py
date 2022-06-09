import json
from requests import Response

"""Methods for requests status checking"""

class Checking():

    """Method for checking status-code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if status_code == response.status_code:
            print("SUCCESS , Status code: " + str(response.status_code))
        else:
            print("FAILURE , Status code: " + str(response.status_code))


    """Method for required data"""
    @staticmethod
    def check_required_data(response: Response,expected_data):
        token = json.loads(response.text)
        assert list(token) == expected_data
        if list(token) == expected_data:
            print("All required data is present")


    """Method for checking values of required data"""
    @staticmethod
    def check_required_data_value(response: Response,field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)

        assert expected_value == check_info
        if expected_value == check_info:
            print(field_name + " Value is VALID")
        else:
            print(field_name + " Value is NOT VALID")