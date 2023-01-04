from src.my_parser import MyParser
import pytest

def test_parser_good_input():
    cmd = ["./306radiator", "3", "1", "1"]
    parser = MyParser(cmd)
    expected_output = [3 ** 2, 3, 1, 1, None, None]

    result = parser.check_cmd()

    assert result == expected_output

def test_parser_good_input_2():
    cmd = ["./306radiator", "3", "1", "1", "1", "1"]
    parser = MyParser(cmd)
    expected_output = [3 ** 2, 3, 1, 1, 1, 1]

    result = parser.check_cmd()

    assert result == expected_output

def test_parser_good_input_3():
    cmd = ["./306radiator", "4", "1", "1", "2", "2"]
    parser = MyParser(cmd)
    expected_output = [4 ** 2, 4, 1, 1, 2, 2]

    result = parser.check_cmd()

    assert result == expected_output

def test_parser_good_input_3():
    cmd = ["./306radiator", "10", "1", "8", "8", "7"]
    parser = MyParser(cmd)
    expected_output = [10 ** 2, 10, 1, 8, 8, 7]

    result = parser.check_cmd()

    assert result == expected_output