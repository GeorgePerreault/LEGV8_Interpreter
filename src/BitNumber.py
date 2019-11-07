from src.Flags import Flags

# Int that simulates having only 64 bits instead of infinite percision like python does
class BitNumber:

    def __init__(self, val=0, n_bits=64):
        self.bits = val & 0xFFFFFFFFFFFFFFFF
        self.n_bits = n_bits

    # Determines what to use for the data model functions
    def __getxy(self, other):
        if type(other) is int:
            y = other
        elif type(other) is BitNumber:
            y = other.bits
        else:
            raise TypeError(f"Bad other in bitnumber __getxy: {type(other)}")
        return self.bits, y

    def __getitem__(self, i):
        if i < 0:
            i = 64 + i
        return (self.bits >> i) % 2

    def __iter__(self):
        n = self.bits
        count = 0

        while n > 0 or count < 64:
            yield n % 2
            count += 1
            n >>= 1

    def __lshift__(self, other):
        x, y = self.__getxy(other)
        return BitNumber(x << y)

    def __rshift__(self, other):
        x, y = self.__getxy(other)
        return BitNumber(x >> y)

    def __and__(self, other):
        x, y = self.__getxy(other)
        return BitNumber(x & y)

    def __or__(self, other):
        x, y = self.__getxy(other)
        return BitNumber(x | y)

    def __xor__(self, other):
        x, y = self.__getxy(other)
        return BitNumber(x ^ y)

    # Allows you to have a carry in and/or have the flag results also be returned 
    def __add__(self, other, give_flags=False, c=0):
        res = 0
        const_one = 1

        for (i, j) in zip(self, other):
            n = i + j + c
            last_c = c
            c = 1 if n > 1 else 0
            res |= const_one if n % 2 == 1 else 0

            const_one <<= 1

        ret = BitNumber(res)

        if give_flags:
            flags = Flags()
            flags.carry = c
            flags.overflow = 1 if last_c != c else 0
            flags.negative = ret[-1]
            flags.zero = 1 if ret == 0 else 0

            return (ret, flags)
        return ret

    # Subtraction is done by doing a + (-b)
    def __sub__(self, other, give_flags=False):
        if type(other) is int:
            return self.__add__(~BitNumber(other), give_flags=give_flags, c=1)
        return self.__add__(~other, give_flags=give_flags, c=1)

    def __eq__(self, other):
        x, y = self.__getxy(other)
        return x == y

    def __invert__(self):
        return BitNumber(0xFFFFFFFFFFFFFFFF ^ self.bits)

    def __int__(self):
        return self.bits

    def __repr__(self):
        return str(self.bits)

