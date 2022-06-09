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

        print("POST-GET Method")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get,200)


        print("PUT Method")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put,200)


        print("PUT-GET Method")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get,200)


        print("DELETE Method")
        result_del = Google_maps_api.del_new_place(place_id)
        Checking.check_status_code(result_del,200)


        print("DELETE-GET Method")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get,404)





