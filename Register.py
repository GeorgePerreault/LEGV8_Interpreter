from BitNumber import BitNumber

ZERO_REG = 31
LINK_REG = 30
FRAME_POINTER = 29
STACK_POINTER = 28


class Register:

    def __init__(self, number: int):
        self.number = number
        self.value = BitNumber()
    
    def assign(self, value):
        if self.number == ZERO_REG:
            return
        if type(value) is int:
            self.value = BitNumber(value)
        else:
            self.value = value

    def __repr__(self):
        return f"X{self.number}:{self.value}"

    def __add__(self, other):
        if type(other) is Register:
            return self.value + other.value
        elif type(other) is int:
            return self.value + BitNumber(other)

    def __sub__(self, other):
        if type(other) is Register:
            return self.value - other.value
        elif type(other) is int:
            return self.value - BitNumber(other)
