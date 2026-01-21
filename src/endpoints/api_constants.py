"""this is a class which contains all the end points

 consider Restfulbooker api we have :-  /booking, booking/id, /auth ,/ping etc"""


class ApiConstants:

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"


    def url_ping(self):
        return "https://restful-booker.herokuapp.com/ping"








