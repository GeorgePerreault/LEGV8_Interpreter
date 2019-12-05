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