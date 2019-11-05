from src.BitNumber import BitNumber

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
    
    def assign(self, other):
        if self.number == ZERO_REG:
            return
        _, y = self.__getxy(other)
        self.value = y

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
        
    def __repr__(self, mode="dec"):
        s = ""
        
        if self.number < 28:
                s += f"X{self.number:02}: "
        else:
            s += f"{special_reg_names(self.number):>3}: "
        
        if mode == "dec":
            if self.value[-1] == 1:
                s += f"-{0xFFFFFFFFFFFFFFFF - self.value.bits + 1:019}"
            else:
                s += f"+{self.value.bits:019}"
        elif mode == "udec":
            s += f"{self.value.bits:020}"
        elif mode == "hex":
            s += f"0x{self.value.bits:016x}"
        elif mode == "bin":
            s += f"0b{self.value.bits:064b}"
        return s

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