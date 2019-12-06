from src.BitNumber import BitNumber
from src.UsefulFuncs import num_as_str, special_reg_names
from src.InstructionSet import ZERO_REG

class Register:

    def __init__(self, number: int):
        self.number = number
        self.value = BitNumber()
    
    def assign(self, other):
        if self.number == ZERO_REG:
            return
        _, y = self.__getxy(other)
        self.value = y

    # Gets the values for the data model ops
    def __getxy(self, other):
        if type(other) is Register:
            y = other.value
        elif type(other) is int:
            y = BitNumber(other)
        elif type(other) is BitNumber:
            y = other
        else:
            raise TypeError(f"Bad other in register __getxy: {type(other)}")
        return self.value, y

    # Allowed modes are dec, udec (unsigned decimal), hex, and bin        
    def __repr__(self, mode="dec"):
        s = ""
        
        if self.number < 28:
                s += f"X{self.number:02}: "
        else:
            s += f"{special_reg_names(self.number):>3}: "

        s += num_as_str(self.value.bits, mode)

        return s

    def __int__(self):
        return int(self.value)

    def __add__(self, other, give_flags=False):
        x, y = self.__getxy(other)
        if give_flags:
            return x.__add__(y, give_flags=True)
        return x + y

    def __sub__(self, other, give_flags=False):
        x, y = self.__getxy(other)
        if give_flags:
            return x.__sub__(y, give_flags=True)
        return x - y

    def __mul__(self, other):
        x, y = self.__getxy(other)
        return x * y

    def __and__(self, other):
        x, y = self.__getxy(other)
        return x & y

    def __or__(self, other):
        x, y = self.__getxy(other)
        return x | y

    def __xor__(self, other):
        x, y = self.__getxy(other)
        return x ^ y

    def __eq__(self, other):
        x, y = self.__getxy(other)
        return x == y