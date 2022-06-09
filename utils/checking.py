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