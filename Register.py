from BitNumber import BitNumber

ZERO_REG = 31
LINK_REG = 30
FRAME_POINTER = 29
STACK_POINTER = 28


def special_reg_names(i):
    if i == 28:
        return "SP"
    if i == 29:
        return "FP"
    if i == 30:
        return "LR"
    if i == 31:
        return "XZR"

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

    def __and__(self, other):
        if type(other) is Register:
            return self.value & other.value
        elif type(other) is int:
            return self.value & BitNumber(other)

    def __or__(self, other):
        if type(other) is Register:
            return self.value | other.value
        elif type(other) is int:
            return self.value | BitNumber(other)

    def __xor__(self, other):
        if type(other) is Register:
            return self.value ^ other.value
        elif type(other) is int:
            return self.value ^ BitNumber(other)

    def __eq__(self, other):
        if type(other) is int:
            return self.value == other
        return self.value == other.value