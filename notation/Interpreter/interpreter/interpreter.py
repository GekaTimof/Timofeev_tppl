from .token import TokenType, Token

class Interpreter():
    # initialization
    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_token = None

    # get current element and move
    def __next(self):
        # end text checking
        if self._pos > len(self._text)-1:
            return Token(TokenType.EOL, "")

        current_char = self._text[self._pos]
        if current_char.isdigit():
            self._pos += 1
            return Token(TokenType.INTEGER, current_char)
        if current_char == "+":
            self._pos += 1
            return Token(TokenType.OPERATOR, current_char)
        if current_char == "-":
            self._pos += 1
            return Token(TokenType.OPERATOR, current_char)
        raise SystemExit("bad token")

    # check token type
    def __check_token(self, type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token = self.__next()
        else:
            raise SystemExit("invalid token order")


    #
    def eval(self, s:str) -> int:
        self._text = s
        self._pos = 0

        # get element
        self._current_token = self.__next()
        # set left element
        left = self._current_token
        # check this element
        self.__check_token(TokenType.INTEGER)

        op = self._current_token
        self.__check_token(TokenType.OPERATOR)

        right = self._current_token
        self.__check_token(TokenType.INTEGER)

        if op.type_ == TokenType.OPERATOR:
            match op.value:
                case "+":
                    return int(left.value) + int(right.value)
                case "-":
                    return int(left.value) - int(right.value)
                case _:
                    raise SyntaxError("wrong operator")
        raise SyntaxError("Interpreter error")
