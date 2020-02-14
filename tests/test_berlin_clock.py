import pytest
from src.berlin_clock import tell_the_time_berlin


def test_tell_the_time_berlin():

    actual_output = tell_the_time_berlin("12:56:01")

    expected_output = "O\nRROO\nRROO\nYYYYYYYYYYY\nYOOO"

    assert actual_output == expected_output