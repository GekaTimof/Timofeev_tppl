import pytest
from collections import deque
from interpreter.interpreter import Interpreter


def test_split_text():
    interpreter = Interpreter("+ 1 2")
    marks, numbers = interpreter._Interpreter__split_text("+ 1 2")
    assert marks == deque(["+"])
    assert numbers == deque(["1", "2"])

def test_solo_mark():
    assert Interpreter("2 + 2").interpreter() == "2 + 2"
    assert Interpreter("20 + 20").interpreter() == "20 + 20"
    assert Interpreter("* 21 2").interpreter() == "21 * 2"
    assert Interpreter("2 2 /").interpreter() == "2 / 2"
    assert Interpreter(" 2  24  -  ").interpreter() == "2 - 24"

def test_multy_mark():
    assert Interpreter("2 + 2 * 7 * 8").interpreter() == "2 + 2 * 7 * 8"
    assert Interpreter("26 + 21 * 71 * 81").interpreter() == "26 + 21 * 71 * 81"
    assert Interpreter("* / + 23 2 53 4").interpreter() == "23 * 2 / 53 + 4"
    assert Interpreter("22 2 61 7 / - +").interpreter() == "22 / 2 - 61 + 7"
    assert Interpreter(" 2  26  - +   5  8  /  ").interpreter() == "2 - 26 + 5 / 8"

def test_unknown_character():
    with pytest.raises(SyntaxError, match="Unknown character - %"):
        interpreter = Interpreter("+ 1 %")
        interpreter.interpreter()

def test_incorrect_argument_ratio():
    with pytest.raises(SyntaxError, match="Incorrect argument ratio"):
        interpreter = Interpreter("+ 1 2 3")
        interpreter.interpreter()

    with pytest.raises(SyntaxError, match="Incorrect argument ratio"):
        interpreter = Interpreter("+ * / 3")
        interpreter.interpreter()
