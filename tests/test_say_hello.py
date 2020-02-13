import pytest
from src.hello_world import say_hello

def test_say_hello():
    actual_value = say_hello()
    expected_value = 'hello'
    
    assert expected_value == actual_value