from CPU import CPU
from LexicalAnalyzer import LexicalAnalyzer

class Driver:
    
    def __init__(self, file):
        self.file = file

    def run(self):
        lex = LexicalAnalyzer(self.file)
        cpu = CPU()

        inst = lex.get_instruction()
        cpu.decode(inst)
        cpu.execute()

        print(cpu)