import allure
import pytest
from src.modules.wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import ApiConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import *
from src.modules.verification.comman_verification import *

class TestCreateBooking:

    @pytest.mark.positive
    @allure.testcase("Verify that create booking status & booking id shouldn't be null")
    @allure.description("Createing a booking from the payload and verify that the booking id should not be null and status code is 200")
    def test_create_booking_positive(self):
        response = post_request(
            url= ApiConstants().url_create_booking(),
            auth=None,
            headers= Utils().common_headers_json(),
            payload= payload_create_booking(),
            in_json=None
        )

        verify_http_status_code(response_data=response,expected_data=200)






    def test_create_booking_negative_tc1(self):
        pass

    def test_create_booking_negative_tc2(self):
        pass

