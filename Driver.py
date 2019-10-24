from CPU import CPU
from LexicalAnalyzer import LexicalAnalyzer, ParserError

class Driver:
    
    def __init__(self, file):
        self.file = file
        self.code = [None]
        self.labels = {}

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

    def run(self):
        start = 1
        try:
            start = self.labels["main"]
        except KeyError:
            pass

        cpu = CPU(pc=start)

        while cpu.pc < len(self.code) and cpu.pc > 0:
            inst = self.code[cpu.pc]
            if not inst:
                cpu.pc += 1
                continue

            cpu.decode(inst, self.labels)
            cpu.execute()

        cpu.reg_dump(mode="dec")
        # self.code_dump()
        # cpu.mem_dump()
