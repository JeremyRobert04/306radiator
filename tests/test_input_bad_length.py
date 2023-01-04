from src.my_parser import MyParser
import pytest

def test_parser_input_not_enough_arg_1(capfd):
    cmd = ["./306radiator", "n"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mUncorrect number of parameters\n\tDo -h to get help.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_not_enough_arg_2(capfd):
    cmd = ["./306radiator", "n", "ir"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mUncorrect number of parameters\n\tDo -h to get help.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_not_enough_arg_4(capfd):
    cmd = ["./306radiator", "n", "ir", "jr", "i"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mUncorrect number of parameters\n\tDo -h to get help.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_too_many_arg(capfd):
    cmd = ["./306radiator", "n", "ir", "jr", "i", "j", "6", "7", "8"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mToo many parameters\n\tDo -h to get help.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84