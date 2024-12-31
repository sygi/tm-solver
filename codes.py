"""Convenience functions for handling codes."""

from typing import Iterator, Self

DIGITS = list(range(1, 6))

def next_digit(digit: int):
    candidate = digit + 1
    if candidate in set(DIGITS):
        return candidate
    return None

CODE_LENGTH = 3

class Code(list[int]):
    def __init__(self, value: list[int] | int):
        if isinstance(value, int):
            value = [value // 100, (value // 10) % 10, value % 10]
        return super().__init__(value)
    def __str__(self):
        return "".join(str(digit) for digit in self)
    def __repr__(self):
        return f"Code({str(self)})"

    def __getitem__(self, index):
        if not isinstance(index, str):
            return super().__getitem__(index)
        mapping = dict(
            blue=0,
            triangle=0,
            yellow=1,
            square=1,
            purple=2,
            circle=2,
        )
        return self[mapping[index]]

    def next_code(self) -> Self | None:
        new_code = list(self)
        for i in range(CODE_LENGTH - 1, -1, -1):
            next_d = next_digit(new_code[i])
            if next_d is not None:
                new_code[i] = next_d
                return type(self)(new_code)
            new_code[i] = min(DIGITS)
        return None


def parse_code(code: str) -> Code:
    return Code([int(digit) for digit in code])

def generate_codes(prefix=None) -> Iterator[Code]:
    """Generates all possible codes."""
    prefix = prefix or []
    if len(prefix) == CODE_LENGTH:
        yield Code(prefix)
        return
    for digit in DIGITS:
        for code in generate_codes(prefix + [digit]):
            yield code
