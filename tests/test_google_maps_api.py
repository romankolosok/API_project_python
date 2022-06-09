import json
from requests import Response
from utils.api import Google_maps_api
from utils.checking import Checking


"""Create/Update/Delete new location"""
class Test_create_place():

    def test_create_new_place(self):
        print("POST Method")
        result_post: Response = Google_maps_api.create_new_place()

        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post,200)
        Checking.check_required_data(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_required_data_value(result_post,"status","OK")


        print("POST-GET Method")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get,200)
        Checking.check_required_data(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_required_data_value(result_get,"address", "29, side layout, cohen 09")


        print("PUT Method")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put,200)
        Checking.check_required_data(result_put,["msg"])
        Checking.check_required_data_value(result_put,"msg","Address successfully updated")


        print("PUT-GET Method")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get,200)
        Checking.check_required_data(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_required_data_value(result_get,"address", "858 Roserail Dr, US")


        print("DELETE Method")
        result_del = Google_maps_api.del_new_place(place_id)
        Checking.check_status_code(result_del,200)
        Checking.check_required_data(result_del,["status"])
        Checking.check_required_data_value(result_del,"status", "OK")


        print("DELETE-GET Method")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get,404)
        Checking.check_required_data(result_get,["msg"])
        Checking.check_required_data_value(result_get,"msg", "Get operation failed, looks like place_id  doesn't exists")


        print("Creating, Changing, Deletion of new location ended")



