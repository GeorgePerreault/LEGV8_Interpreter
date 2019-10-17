class TTS:
    COMMA = 0
    REGISTER = 1
    IMMEDIATE = 2
    LABEL = 3
    OPEN_SQUARE = 4
    CLOSE_SQUARE = 5
    HASH = 6

TOKEN_TYPE_NAMES = (
    "COMMA",
    "REGISTER",
    "IMMEDIATE",
    "LABEL",
    "OPEN_SQUARE",
    "CLOSE_SQUARE",
    "HASH"
)

r_r_r = (TTS.REGISTER, TTS.COMMA, TTS.REGISTER, TTS.COMMA, TTS.REGISTER)
r_r_i = (TTS.REGISTER, TTS.COMMA, TTS.REGISTER, TTS.COMMA, TTS.HASH, TTS.IMMEDIATE)
mem = (TTS.REGISTER, TTS.COMMA, TTS.OPEN_SQUARE, TTS.REGISTER, TTS.COMMA, TTS.HASH, TTS.IMMEDIATE, TTS.CLOSE_SQUARE)
br = (TTS.LABEL,)
cbr = (TTS.REGISTER, TTS.COMMA, TTS.LABEL)

INSTRUCTION_SET = {
    "add": r_r_r,
    "addi": r_r_i,
    "adds": r_r_r,
    "addis": r_r_i,

    "sub": r_r_r,
    "subi": r_r_i,
    "subs": r_r_r,
    "subis": r_r_i,

    "and": r_r_r,
    "andi": r_r_i,

    "or": r_r_r,
    "ori": r_r_i,

    "eor": r_r_r,
    "eori": r_r_i,

    "lsl": r_r_i,
    "lsr": r_r_i,

    "ldur": mem,
    "ldurw": mem,
    "ldurh": mem,
    "ldurb": mem,

    "stur": mem,
    "sturw": mem,
    "sturh": mem,
    "sturb": mem,

    "b": br,
    "cbz": cbr,
    "cbnz": cbr
}