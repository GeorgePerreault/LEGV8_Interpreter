from src.Driver import Driver
from src.DebugCommandParser import DebugCommandParser
from src.Exceptions import DebugCommandError

class Debugger():

    def __init__(self, driver):
        self.driver = driver
        self.action = "c"
        self.param = None
        self.act_before_broke = None
        self.dcp = DebugCommandParser()

    def set_dcp_vals(self, ret):
        self.action = ret[0]
        if self.action == "m":
            self.driver.mode = ret[1]

        if self.action in {"l", "p"}:
            self.param = ret[1]
        else:
            self.param = None

    # Returns a bool of whether or not the command worked
    def input_ask(self):
        s = input("")
        if s == "":
            # If you enter nothing, use the last action
            # Breakpoints change the action so I have to adjust for that
            self.action = self.act_before_broke if self.act_before_broke else self.action
            return True
        self.act_before_broke = None

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
    def handle_n(self):
        self.driver.reg_dump()
        self.driver.print_cur()
        self.get_action()

    # List command lists nearby lines
    def handle_l(self):
        print(self.param)
        if self.param:
            self.driver.print_inst(self.param, spread=3)
        else:
            self.driver.print_cur(spread=3)
        self.get_action()

    # Mode command changes the current print mode
    def handle_m(self):
        self.driver.reg_dump()
        self.get_action()

    def handle_h(self):
        print("----------HELP----------")
        print("Valid commands: \n\ncontinue / c\nnext / n\nlist / l\nmode / m")
        print("------------------------")
        self.get_action()

    def handle_p(self):
        print("----Memory----")
        self.driver.mem_dump(register_num=self.param)
        self.get_action()

    def debug(self):
        self.driver.setup()
        inst = self.driver.cur_inst()

        while self.driver.active():
            if inst and self.action == "n":
                self.handle_n()

            if inst and self.action == "l":
                self.handle_l()
                continue
            
            if inst and self.action == "m":
                self.handle_m()
                continue

            if inst and self.action == "h":
                self.handle_h()
                continue
            
            if inst and self.action == "p":
                self.handle_p()
                continue

            # Beacuse continue is none of these, it will cause the program to run un-interrupted 

            self.driver.exe_next()

            if self.driver.active():
                inst = self.driver.cur_inst()
            else:
                inst = None
                
            if inst and inst.b_point:
                # Stop on breakpoints
                self.act_before_broke = self.action
                self.action = "n"
