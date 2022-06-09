from utils.http_methods import Http_method

"""Methods for testing google maps api"""

base_url = "https://rahulshettyacademy.com"  #base url
request_key = "?key=qaclick123"  #common key for all requests

class Google_maps_api():

    """Method for creation of new location"""
    @staticmethod
    def create_new_place():

        json_for_new_place_creation = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }  # Body element for method POST

        post_resource = "/maps/api/place/add/json"   # Resource for method POST

        post_url = base_url + post_resource + request_key
        print(post_url)

        result_post = Http_method.post(post_url, json_for_new_place_creation)
        print(result_post.text)

        return result_post

    """Method for checking new location"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + request_key + "&place_id=" + place_id
        print(get_url)

        result_get = Http_method.get(get_url)
        print(result_get.text)

        return result_get

    """Method for updating new location"""

    @staticmethod
    def put_new_place(place_id):

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "858 Roserail Dr, US",
            "key": "qaclick123"

        }

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + request_key
        print(put_url)

        result_put = Http_method.put(put_url,json_for_update_new_location)
        print(result_put.text)

        return result_put

    """Delete new place"""

    @staticmethod
    def del_new_place(place_id):

        json_del_new_place = {
            "place_id": place_id
        }

        del_resource = "/maps/api/place/delete/json"
        del_url = base_url + del_resource + request_key
        print(del_url)

        result_del = Http_method.delete(del_url,json_del_new_place)
        print(result_del.text)

        return result_del




