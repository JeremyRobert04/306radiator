from src.my_parser import MyParser
import pytest

def test_parser_no_input_code():
    cmd = ["./306radiator"]
    parser = MyParser(cmd)

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    assert excinfo.value.code == 84

def test_parser_no_input_msg(capfd):
    cmd = ["./306radiator"]
    parser = MyParser(cmd)
    expected_err_msg = "\033[91mERROR:\t\033[0mMissing parameters\n\tDo -h to get help.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_err_msg
