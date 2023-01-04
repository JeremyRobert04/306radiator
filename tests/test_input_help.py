from src.my_parser import MyParser
import pytest

def test_parser_input_help(capfd):
    cmd = ["./306radiator", "--help"]
    parser = MyParser(cmd)
    expected_output = "USAGE\n\t./306radiator n ir jr [i j]\n\nDESCRIPTION\n\tn\t\tsize of the room\n\t(ir, jr)\tcoordinates of the radiator\n\t[i, j]\t\tOPTIONNAL: coordinates of a point in the room\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert out == expected_output
    assert excinfo.value.code == 0

def test_parser_input_h(capfd):
    cmd = ["./306radiator", "-h"]
    parser = MyParser(cmd)
    expected_output = "USAGE\n\t./306radiator n ir jr [i j]\n\nDESCRIPTION\n\tn\t\tsize of the room\n\t(ir, jr)\tcoordinates of the radiator\n\t[i, j]\t\tOPTIONNAL: coordinates of a point in the room\n"

    with pytest.raises(SystemExit) as excinfo:
        parser.check_cmd()

    out, err = capfd.readouterr()
    assert out == expected_output
    assert excinfo.value.code == 0

def test_parser_display_help_cmd(capfd):
    expected_output = "USAGE\n\t./306radiator n ir jr [i j]\n\nDESCRIPTION\n\tn\t\tsize of the room\n\t(ir, jr)\tcoordinates of the radiator\n\t[i, j]\t\tOPTIONNAL: coordinates of a point in the room\n"
    parser = MyParser()

    parser.display_help()
    out, err = capfd.readouterr()
    assert out == expected_output
