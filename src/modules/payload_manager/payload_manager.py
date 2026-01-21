def payload_create_booking():
    paylod ={
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return paylod


def payload_update_booking():
    paylod ={
        "firstname": "megha",
        "lastname": "varun",
        "totalprice": 111,
        "depositpaid": true,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return paylod

def payload_create_token():
    paylod ={
        "username": "admin",
        "password": "password123"
    }
    return paylod

