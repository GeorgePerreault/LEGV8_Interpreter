from src.Driver import Driver
from src.DebugCommandParser import *

class Debugger():

    def __init__(self, driver):
        self.driver = driver
        self.action = "c"
        self.spread = 3
        self.dcp = DebugCommandParser()

    def set_dcp_vals(self, ret):
        self.action = ret[0]
        self.driver.mode = ret[1] if ret[1] else self.driver.mode
        self.spread = ret[2]

    def input_ask(self):
        s = input("")
        if s == "":
            return True

        try:
            self.set_dcp_vals(self.dcp.parse_command(s))
        except DebugCommandError as e:
            print(e)
            return False

        return True

    def get_action(self):
        while not self.input_ask():
            pass

    def handle_s(self):
        self.driver.reg_dump()
        self.driver.print_cur()
        self.get_action()

    def handle_l(self):
        self.driver.print_cur(spread=self.spread if self.spread else 3)
        self.get_action()

    def handle_m(self):
        self.driver.reg_dump()
        self.get_action()

    def debug(self):
        self.driver.setup()
        inst = self.driver.cur_inst()

        while self.driver.active():
            if inst and self.action == "s":
                self.handle_s()

            if inst and self.action == "l":
                self.handle_l()
                continue
            
            if inst and self.action == "m":
                self.handle_m()
                continue

            self.driver.exe_next()

            inst = self.driver.cur_inst()
            if inst and inst.b_point:
                self.action = "s"
