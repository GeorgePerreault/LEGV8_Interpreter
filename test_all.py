import pytest

from InstructionSet import INSTRUCTION_SET
from OpcodeTable import OpcodeTable
from Memory import Memory
from MemOps import Load, Store
from BitNumber import BitNumber
from CPU import CPU

def all_in_both():
    opct = OpcodeTable(CPU())

    if len(INSTRUCTION_SET) != len(opct.OPCODE_TABLE):
        return False

    for opcode in INSTRUCTION_SET.keys():
        if opcode not in opct.OPCODE_TABLE:
            return False
    return True

def mem_swap(v, e, n_bytes=8):
    mem = Memory()
    ld = Load(mem, n_bytes=n_bytes)
    st = Store(mem, n_bytes=n_bytes)

    class dummy_reg():
        def __init__(self, v):
            self.value = v
        def assign(self, v):
            pass
    
    x = dummy_reg(v)
    st.execute(x, 0, 0)
    res = ld.execute(x, 0, 0)

    return res == e


def test_bits():
    x = BitNumber(1)
    assert x - x == 0
    y = BitNumber(1)
    assert x == y
    assert x - y == 0
    assert x + y == 2
    assert x + y == BitNumber(2)
    
    x = BitNumber(16)
    y = BitNumber(8)
    assert x - y == 8
    assert (x + y + y) == 0x20

def test_tables():
    assert all_in_both()

def test_memory():
    assert mem_swap(0xABCD1234ABCD1234, 0xABCD1234ABCD1234)
    assert mem_swap(0b100000000, 0, n_bytes=1)
    assert mem_swap(0b100000000, 0b100000000, n_bytes=2)