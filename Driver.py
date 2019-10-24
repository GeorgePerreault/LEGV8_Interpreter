from CPU import CPU
from LexicalAnalyzer import LexicalAnalyzer, ParserError

class Driver:
    
    def __init__(self, file):
        self.file = file
        self.code = [None]
        self.labels = {}
        self.cpu = None

    def __print_inst(self, line, inst):
        if not inst:
            inst = ""
        print(f"{line:>03} {inst}")
    
    def __print_range(self, start, stop):
        if stop > len(self.code):
            stop = len(self.code)
        if start <= 0:
            start = 1

        for i in range(start, stop):
            self.__print_inst(i, self.code[i])

    def cur_inst(self):
        return self.code[self.cpu.pc]

    def print_cur(self, spread=None):
        if spread:
            self.__print_range(self.cpu.pc - spread, self.cpu.pc + spread + 1)
        else:
            self.__print_inst(self.cpu.pc, self.cur_inst())

    def code_dump(self):
        self.__print_range(0, len(self.code))

    def reg_dump(self, mode="dec"):
        self.cpu.reg_dump(mode=mode)

    def mem_dump(self):
        self.cpu.mem_dump()

    def generate_code(self):
        lex = LexicalAnalyzer(self.file)
        line_num = 0

        while True:
            line_num += 1

            try:
                inst = lex.get_instruction()            
            except ParserError as e:
                raise ParserError(f"{line_num:>03} {e}")

            self.code.append(inst)

            if inst is None:
                if lex.eof:
                    break
                continue

            if lex.has_label:
                self.labels[lex.get_label()] = line_num

    def setup(self):
        start = 1
        try:
            start = self.labels["main"]
        except KeyError:
            pass

        self.cpu = CPU(pc=start)

    def active(self):
        return self.cpu.pc < len(self.code) and self.cpu.pc > 0 

    def run(self):
        self.setup()

        while self.active():
            self.exe_next()

        self.reg_dump(mode="dec")
        self.code_dump()
        # self.mem_dump()

    def exe_next(self):
        inst = self.cur_inst()
        if not inst:
            self.cpu.pc += 1
            return

        self.cpu.decode(inst, self.labels)
        self.cpu.execute()

