import pytest
import allure

@allure.title("Varify Pass ✅ ! Framework is working")

def test_sample_pass():
    assert True==True

@allure.title("verify fail ❌ ! Framework is working")

def test_sample_fail():
    assert True==False
