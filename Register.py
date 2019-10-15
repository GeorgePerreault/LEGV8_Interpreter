from Token import Token, IMMEDIATE

class Register:
    ZERO_REG = 31
    LINK_REG = 30

    def __init__(self, number: int):
        self.number = number
        self.value = 2
    
    def assign(self, value):
        self.value = (value if self.number != Register.ZERO_REG else 0)

    def __repr__(self):
        return f"X{self.number}:{self.value}"

    def __add__(self, other):
        if type(other) is Register:
            return self.value + other.value
        elif type(other) is Token and other.type == IMMEDIATE:
            return self.value + other.i_val
