class Flags:

    def __init__(self):
        self.carry = 0
        self.overflow = 0
        self.negative = 0
        self.zero = 0

    def set_flags(self, flags):
        if type(flags) is tuple:
            self.carry, self.overflow, self.negative, self.zero = flags
        elif type(flags) is Flags:
            self.carry = flags.carry
            self.overflow = flags.overflow
            self.negative = flags.negative
            self.zero = flags.zero
    
    def __str__(self):
        return f"c = {self.carry}\no = {self.overflow}\nn = {self.negative}\nz = {self.zero}"
