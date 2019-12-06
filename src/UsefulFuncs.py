from src.InstructionSet import STACK_POINTER, FRAME_POINTER, LINK_REG, ZERO_REG

def special_reg_names(i):
    if i == STACK_POINTER:
        return "SP"
    if i == FRAME_POINTER:
        return "FP"
    if i == LINK_REG:
        return "LR"
    if i == ZERO_REG:
        return "XZR"

def num_as_str(n, mode):
    s = ""

    if mode == "dec":
        if n > 0x7FFFFFFFFFFFFFFF:
            s += f"-{0xFFFFFFFFFFFFFFFF - n + 1:019}"
        else:
            s += f"+{n:019}"
    elif mode == "udec":
        s += f"{n:020}"
    elif mode == "hex":
        s += f"0x{n:016x}"
    elif mode == "bin":
        s += f"0b{n:064b}"
    return s

def get_reg_num_from_str(s):
    if s[0] == "x":
        if s[1:] == "zr":
            return ZERO_REG
        try:
            ret = int(s[1:])
            if ret < 0 or ret > 31:
                raise ValueError
            return ret
        except ValueError:
            return None

    elif s == "lr":
        return LINK_REG
    elif s == "fp":
        return FRAME_POINTER
    elif s == "sp":
        return STACK_POINTER

    return None