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

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + request_key + "&place_id=" + place_id
        print(get_url)

        result_get = Http_method.get(get_url)
        print(result_get.text)

        return result_get

