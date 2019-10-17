
class BitNumber:

    def __init__(self, val=0, n_bits=64):
        self.carry = 0
        self.overflow = 0
        self.negative = 0
        self.zero = 0

        self.bits = val & 0xFFFFFFFFFFFFFFFF
        self.n_bits = n_bits

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
        if type(other) is int:
            return BitNumber(self.bits << other)
        return BitNumber(self.bits << int(other.bits))

    def __rshift__(self, other):
        if type(other) is int:
            return BitNumber(self.bits >> other)
        return BitNumber(self.bits >> int(other.bits))

    def __and__(self, other):
        if type(other) is int:
            return BitNumber(self.bits & other)
        return BitNumber(self.bits & other.bits)

    def __or__(self, other):
        if type(other) is int:
            return BitNumber(self.bits | other)
        return BitNumber(self.bits | other.bits)

    def __xor__(self, other):
        if type(other) is int:
            return BitNumber(self.bits ^ other)
        return BitNumber(self.bits ^ other.bits)

    def __add__(self, other, c=0):
        if type(other) is int:
            return self.__add__(BitNumber(other))

        res = 0
        bit_num = 0

        for (i, j) in zip(self, other):
            n = i + j + c
            
            last_c = c
            c = 1 if n > 1 else 0
            res |= (1 << bit_num) if n % 2 == 1 else 0

            bit_num += 1

        ret = BitNumber(res)

        ret.carry = c
        ret.overflow = 1 if last_c != c else 0
        ret.negative = ret[-1]
        ret.zero = 1 if ret == 0 else 0

        return ret

    def __eq__(self, other):
        if type(other) is int:
            return self.bits == other
        return self.bits == other.bits

    def __invert__(self):
        return BitNumber(0xFFFFFFFFFFFFFFFF ^ self.bits)

    def __sub__(self, other):
        if type(other) is int:
            return self.__add__(~BitNumber(other), c=1)
        return self.__add__(~other, c=1)

    def __int__(self):
        return self.bits

    def __repr__(self):
        return str(self.bits)

