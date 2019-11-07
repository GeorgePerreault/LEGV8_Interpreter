from src.CPU import CPU
from src.LexicalAnalyzer import LexicalAnalyzer, ParserError

class Driver:
    
    def __init__(self, file, mode="dec"):
        self.file = file
        self.code = [None]
        self.labels = {}
        self.cpu = None
        self.mode = mode

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

    # Prints the current instruction along with spread instructions above and below it 
    def print_cur(self, spread=None):
        if spread:
            self.__print_range(self.cpu.pc - spread, self.cpu.pc + spread + 1)
        else:
            self.__print_inst(self.cpu.pc, self.cur_inst())

    def code_dump(self):
        self.__print_range(0, len(self.code))

    def reg_dump(self, row_size=None):
        if not row_size:
            row_size = 2 if self.mode == "bin" else 4
        self.cpu.reg_dump(mode=self.mode, row_size=row_size)

    def mem_dump(self):
        self.cpu.mem_dump()

    # Fills out self.code and self.labels by parsing the input 
    # Must be run before execution
    def generate_code(self):
        lex = LexicalAnalyzer(self.file)
        line_num = 0

        while not lex.eof:
            line_num += 1

            try:
                inst = lex.get_instruction()            
            except ParserError as e:
                raise ParserError(f"{line_num:>03} {e}")

            self.code.append(inst)

            if lex.has_label:
                self.labels[lex.get_label()] = line_num

    # If there's a main label we start there, otherwise at line 1
    def setup(self):
        start = 1
        try:
            start = self.labels["main"]
        except KeyError:
            pass

        self.cpu = CPU(pc=start)

    # Returns if the execution is still in bounds or not
    def active(self):
        return self.cpu.pc < len(self.code) and self.cpu.pc > 0 

    def run(self):
        self.setup()

        while self.active():
            self.exe_next()

    def exe_next(self):
        inst = self.cur_inst()
        if not inst:
            self.cpu.pc += 1
            return

        self.cpu.decode(inst, self.labels)
        self.cpu.execute()

