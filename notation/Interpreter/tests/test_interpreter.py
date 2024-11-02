import pytest
from interpreter.interpreter import Interpreter

# scope="function" - create new interpreter for each function
@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:
    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4
        assert interpreter.eval("4+3") == 7


    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0
        assert interpreter.eval("4-3") == 1