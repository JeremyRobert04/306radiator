from src.main import main
import pytest

def test_main_good_input_1():
    cmd = ["./306radiator", "3", "1", "1"]
    with pytest.raises(SystemExit) as excinfo:
        main(cmd)

    assert excinfo.value.code == 0

def test_main_good_input_2():
    cmd = ["./306radiator", "3", "1", "1", "1", "1"]
    with pytest.raises(SystemExit) as excinfo:
        main(cmd)

    assert excinfo.value.code == 0

def test_main_bad_input_1():
    cmd = ["./306radiator", "2", "1"]
    with pytest.raises(SystemExit) as excinfo:
        main(cmd)

    assert excinfo.value.code == 84

def test_main_bad_input_2():
    cmd = ["./306radiator", "3", "1", "0", "2", "2"]
    with pytest.raises(SystemExit) as excinfo:
        main(cmd)

    assert excinfo.value.code == 84

def test_main_bad_input_3():
    cmd = ["./306radiator", "3", "1", "1", "-2", "0"]
    with pytest.raises(SystemExit) as excinfo:
        main(cmd)

    assert excinfo.value.code == 84
