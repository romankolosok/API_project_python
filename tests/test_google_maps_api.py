from requests import Response

from utils.api import Google_maps_api


"""Create/Update/Delete new location"""
class Test_create_place():

    def test_create_new_place(self):
        print("POST Method")
        result_post: Response = Google_maps_api.create_new_place()

