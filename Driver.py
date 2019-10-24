from CPU import CPU
from LexicalAnalyzer import LexicalAnalyzer, ParserError

class Driver:
    
    def __init__(self, file):
        self.file = file
        self.code = [None]
        self.labels = {}
        self.cpu = None

    def code_dump(self):
        for (line, inst) in enumerate(i for i in self.code if i):
            print(f"{line:>03} {inst}")

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

    def next_inst(self):
        inst = self.code[self.cpu.pc]
        if not inst:
            self.cpu.pc += 1
            return

        self.cpu.decode(inst, self.labels)
        self.cpu.execute()


    def run(self):
        self.setup()
        
        while self.cpu.pc < len(self.code) and self.cpu.pc > 0:
            self.next_inst()
        
        self.cpu.reg_dump(mode="dec")
        # self.code_dump()
        # cpu.mem_dump()
