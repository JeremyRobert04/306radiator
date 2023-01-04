from src.my_parser import MyParser
import pytest

def test_parser_input_letters_in_args_1(capfd):
    cmd = ["./306radiator", "n", "ir", "jr"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mParameters should only contains number.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_letters_in_args_2(capfd):
    cmd = ["./306radiator", "0", "1", "jr"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mParameters should only contains number.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_letters_in_args_3(capfd):
    cmd = ["./306radiator", "0", "az", "2"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mParameters should only contains number.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_letters_in_args_4(capfd):
    cmd = ["./306radiator", "az", "1", "2"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mParameters should only contains number.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_letters_in_args_5(capfd):
    cmd = ["./306radiator", "123az", "1", "2"]
    parser = MyParser(cmd)
    expected_output = "\033[91mERROR:\t\033[0mParameters should only contains number.\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_room_size_1(capfd):
    cmd = ["./306radiator", "0", "2", "2"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mRoom size should be greater than 2 but got: {cmd[1]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_room_size_2(capfd):
    cmd = ["./306radiator", "1", "2", "2"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mRoom size should be greater than 2 but got: {cmd[1]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_room_size_3(capfd):
    cmd = ["./306radiator", "-1", "2", "2"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mRoom size should be greater than 2 but got: {cmd[1]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_room_size_4(capfd):
    cmd = ["./306radiator", "2", "2", "2"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mRoom size should be greater than 2 but got: {cmd[1]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

"""
Subject:
    We write ir and jr the radiator's coordinates, with 1 ≤ ir, jr ≤ N - 2.
"""
def test_parser_input_bad_radiator_x_pos_1(capfd):
    cmd = ["./306radiator", "3", "0", "1"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mX coordinate for radiator should be between 1 <= X <= {int(cmd[1]) - 2}, but got X: {cmd[2]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_radiator_x_pos_2(capfd):
    cmd = ["./306radiator", "3", "-1", "1"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mX coordinate for radiator should be between 1 <= X <= {int(cmd[1]) - 2}, but got X: {cmd[2]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_radiator_x_pos_3(capfd):
    cmd = ["./306radiator", "3", "5", "1"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mX coordinate for radiator should be between 1 <= X <= {int(cmd[1]) - 2}, but got X: {cmd[2]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_radiator_x_pos_4(capfd):
    cmd = ["./306radiator", "3", "5000", "1"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mX coordinate for radiator should be between 1 <= X <= {int(cmd[1]) - 2}, but got X: {cmd[2]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_radiator_y_pos_1(capfd):
    cmd = ["./306radiator", "3", "1", "0"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mY coordinate for radiator should be between 1 <= Y <= {int(cmd[1]) - 2}, but got Y: {cmd[3]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_radiator_y_pos_2(capfd):
    cmd = ["./306radiator", "3", "1", "-1"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mY coordinate for radiator should be between 1 <= Y <= {int(cmd[1]) - 2}, but got Y: {cmd[3]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_radiator_y_pos_3(capfd):
    cmd = ["./306radiator", "3", "1", "5"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mY coordinate for radiator should be between 1 <= Y <= {int(cmd[1]) - 2}, but got Y: {cmd[3]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_radiator_y_pos_4(capfd):
    cmd = ["./306radiator", "3", "1", "5000"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mY coordinate for radiator should be between 1 <= Y <= {int(cmd[1]) - 2}, but got Y: {cmd[3]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

"""
Subject:
    The boundary conditions are written, with 0 ≤ i, j ≤ N - 1:
"""
def test_parser_input_bad_point_x_pos_1(capfd):
    cmd = ["./306radiator", "3", "1", "1", "-1", "2"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mX coordinate for position should be between 1 <= X <= {int(cmd[1]) - 2}, but got X: {cmd[4]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_point_x_pos_2(capfd):
    cmd = ["./306radiator", "3", "1", "1", "-1000", "2"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mX coordinate for position should be between 1 <= X <= {int(cmd[1]) - 2}, but got X: {cmd[4]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_point_x_pos_3(capfd):
    cmd = ["./306radiator", "3", "1", "1", "10000", "2"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mX coordinate for position should be between 1 <= X <= {int(cmd[1]) - 2}, but got X: {cmd[4]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_point_x_pos_4(capfd):
    cmd = ["./306radiator", "3", "1", "1", "0", "2"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mX coordinate for position should be between 1 <= X <= {int(cmd[1]) - 2}, but got X: {cmd[4]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_point_y_pos_1(capfd):
    cmd = ["./306radiator", "3", "1", "1", "1", "-1"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mY coordinate for position should be between 1 <= Y <= {int(cmd[1]) - 2}, but got Y: {cmd[5]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_point_y_pos_2(capfd):
    cmd = ["./306radiator", "3", "1", "1", "1", "-1000"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mY coordinate for position should be between 1 <= Y <= {int(cmd[1]) - 2}, but got Y: {cmd[5]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_point_y_pos_3(capfd):
    cmd = ["./306radiator", "3", "1", "1", "1", "10000"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mY coordinate for position should be between 1 <= Y <= {int(cmd[1]) - 2}, but got Y: {cmd[5]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84

def test_parser_input_bad_point_y_pos_4(capfd):
    cmd = ["./306radiator", "3", "1", "1", "1", "0"]
    parser = MyParser(cmd)
    expected_output = f"\033[91mERROR:\t\033[0mY coordinate for position should be between 1 <= Y <= {int(cmd[1]) - 2}, but got Y: {cmd[5]}\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert err == expected_output
    assert excinfo.value.code == 84