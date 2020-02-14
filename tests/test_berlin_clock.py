import pytest
from src.berlin_clock import tell_the_time_berlin
from src.berlin_clock import get_row_1


def test_tell_the_time_berlin():

    actual_output = tell_the_time_berlin("12:56:01")

    expected_output = "O\nRROO\nRROO\nYYYYYYYYYYY\nYOOO"

    assert actual_output == expected_output


def test_get_row_1():

    actual_output = get_row_1(8)
    expected_output = "Y"
    assert actual_output == expected_output


def test_get_row_2():

    actual_output = get_row_2(21)
    expected_output = "RRRR"
    assert actual_output == expected_output

def test_get_row_3():

    actual_output = get_row_3(21)
    expected_output = "ROOO"
    assert actual_output == expected_output

def test_get_row_4():

    actual_output = get_row_4(53)
    expected_output = "YYYYYYYYYYO"
    assert actual_output == expected_output

def test_get_row_5():

    actual_output = get_row_5(53)
    expected_output = "YYYO"
    assert actual_output == expected_output


def test_create_row_string():

    actual_output = create_row_string(8,4,"Y")
    expected_output = "YYYYOOOO"
    assert actual_output == expected_output    