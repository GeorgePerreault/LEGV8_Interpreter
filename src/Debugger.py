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

    # Returns a bool of whether or not the command worked
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
        # Keep asking for a command until one works
        while not self.input_ask():
            pass
    
    # Step command goes one line down
    def handle_s(self):
        self.driver.reg_dump()
        self.driver.print_cur()
        self.get_action()

    # List command lists nearby lines
    def handle_l(self):
        self.driver.print_cur(spread=self.spread if self.spread else 3)
        self.get_action()

    # Mode command changes the current print mode
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
            
            # Beacuse continue is none of these, it will cause the program to run un-interrupted 

            self.driver.exe_next()

            inst = self.driver.cur_inst()
            if inst and inst.b_point:
               # Stop on breakpoints
                self.action = "s"
