from collections import deque

class Interpreter:
    def __init__(self, text: str):
        self.marks = deque
        self.numbers = deque
        self.marks, self.numbers = self.__split_text(text)

    def __split_text(self, text: str) -> (deque, deque):
        marks = deque()
        numbers = deque()
        marks_arr = ["+", "-", "*", "/"]

        for elem in text.split():
            if elem.isnumeric():
                numbers.append(elem)
            elif elem in marks_arr:
                marks.append(elem)
            else:
                raise SyntaxError(f"Unknown character - {elem}")

        return (marks, numbers)


    def interpreter(self) -> str:
        result = ""

        if len(self.marks) + 1 == len(self.numbers):
            for i in range(len(self.marks)):
                result += f"{self.numbers.popleft()}"
                result += f" {self.marks.popleft()} "
            result += f"{self.numbers.popleft()}"
        else:
            raise SyntaxError(f"Incorrect argument ratio")

        return result
