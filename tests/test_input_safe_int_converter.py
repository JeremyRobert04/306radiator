from src.my_parser import MyParser
import pytest

def test_parser_safe_int_converter_bad_1():
    parser = MyParser()

    result = parser.safeIntConverter("")

    assert result == None

def test_parser_safe_int_converter_bad_2():
    parser = MyParser()

    result = parser.safeIntConverter("azertyuiop")

    assert result == None

def test_parser_safe_int_converter_bad_3():
    parser = MyParser()

    result = parser.safeIntConverter("123azertyuiop")

    assert result == None

def test_parser_safe_int_converter_good_1():
    parser = MyParser()

    result = parser.safeIntConverter("0")

    assert result == 0

def test_parser_safe_int_converter_good_2():
    parser = MyParser()

    result = parser.safeIntConverter("0123")

    assert result == 123

def test_parser_safe_int_converter_good_3():
    parser = MyParser()

    result = parser.safeIntConverter("-10")

    assert result == -10

def test_parser_safe_int_converter_good_4():
    parser = MyParser()

    result = parser.safeIntConverter("1234567890")

    assert result == 1234567890