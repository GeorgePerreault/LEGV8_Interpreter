ZERO = (0,) * 64

class BitNumber:

    def __init__(self, val=ZERO, n_bits=64):
        self.carry = 0
        self.overflow = 0
        self.negative = 0
        self.zero = 0

        if type(val) is tuple:
            if len(val) != 64:
                raise Exception("Don't make a non 64-bit number")
            self.bits = val
        else:
            self.bits = self.as_bits(val)
        self.n_bits = n_bits

    def bit_yielder(self, v):
        count = 0
        while v > 0 or count < 64:
            yield v % 2
            count += 1
            v >>= 1

    def as_bits(self, v):
        return tuple(self.bit_yielder(v))

    def __getitem__(self, i):
        return self.bits[i]

    def __iter__(self):
        for bit in self.bits:
            yield bit

    def __add__(self, other):
        if type(other) is int:
            return self.__add__(self.as_bits(other))
        
        res = []
        c = 0
        for i in range(len(self.bits)):
            n = self[i] + other[i] + c
            c = 1 if n > 1 else 0
            res.append(1 if n % 2 == 1 else 0)

        ret = BitNumber(tuple(res))
        
        ret.carry = c
        ret.overflow = 1 if (self[-1] == other[-1] and ret[-1] != self[-1]) else 0
        ret.negative = ret[-1]
        ret.zero = 1 if 1 not in res else 0

        return ret

    def __repr__(self):
        return "".join(str(i) for i in reversed(self.bits))

