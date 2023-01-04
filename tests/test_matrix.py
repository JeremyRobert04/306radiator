from src.radiator import Radiator
import pytest

def test_radiator_1(capfd):
    radiator = Radiator(4, 16, 1, 1, None, None)
    expected_matrix ='1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n\
0\t1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n\
0\t0\t1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n\
0\t0\t0\t1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n\
0\t0\t0\t0\t1\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n\
0\t4\t0\t0\t4\t-16\t4\t0\t0\t4\t0\t0\t0\t0\t0\t0\n\
0\t0\t4\t0\t0\t4\t-16\t4\t0\t0\t4\t0\t0\t0\t0\t0\n\
0\t0\t0\t0\t0\t0\t0\t1\t0\t0\t0\t0\t0\t0\t0\t0\n\
0\t0\t0\t0\t0\t0\t0\t0\t1\t0\t0\t0\t0\t0\t0\t0\n\
0\t0\t0\t0\t0\t4\t0\t0\t4\t-16\t4\t0\t0\t4\t0\t0\n\
0\t0\t0\t0\t0\t0\t4\t0\t0\t4\t-16\t4\t0\t0\t4\t0\n\
0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1\t0\t0\t0\t0\n\
0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1\t0\t0\t0\n\
0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1\t0\t0\n\
0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1\t0\n\
0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t1\n\n\
0.0\n0.0\n0.0\n0.0\n0.0\n21.9\n6.3\n0.0\n0.0\n6.3\n\
3.1\n0.0\n0.0\n0.0\n0.0\n0.0\n'

    radiator.radiator()

    out, err = capfd.readouterr()
    assert out == expected_matrix

def test_radiator_2(capfd):
    radiator = Radiator(4, 4 ** 2, 1, 1, 2, 2)
    expected_output = '3.1\n'

    radiator.radiator()

    out, err = capfd.readouterr()
    assert out == expected_output

def test_radiator_3(capfd):
    radiator = Radiator(5, 5 ** 2, 1, 2, 3, 2)
    expected_output = '3.3\n'

    radiator.radiator()

    out, err = capfd.readouterr()
    assert out == expected_output

def test_radiator_4(capfd):
    radiator = Radiator(8, 8 ** 2, 4, 6, 3, 6)
    expected_output = '9.4\n'

    radiator.radiator()

    out, err = capfd.readouterr()
    assert out == expected_output

def test_radiator_5(capfd):
    radiator = Radiator(12, 12 ** 2, 3, 9, 1, 6)
    expected_output = '2.5\n'

    radiator.radiator()

    out, err = capfd.readouterr()
    assert out == expected_output