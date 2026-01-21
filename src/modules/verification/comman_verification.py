"""Common  verification
1. hhtp status code
2. header
3. data verification
4.json schema       """

def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code == expected_data, "Failed to match the status code "


def verify_json_key_for_not_null(response_data,expected_data):
    assert response_data.status_code == expected_data, "Failed to match the json key "
