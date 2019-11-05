from src.Driver import Driver

ALLOWED_ACTIONS = ("continue", "step", "list", "mode", "c", "s", "l", "m")

class Debugger():

    def __init__(self, driver):
        self.driver = driver
        self.action = "c"
        self.spread = None

    def input_ask(self):
        s = input("")
        if s == "":
            return True

        s = s.split()
        self.action = s[0]
        self.param = s[1] if len(s) == 2 else None

        if self.param:
            if self.action[0] == "l":
                try:
                    self.spread = int(self.param)
                except ValueError:
                    return False
            elif self.action[0] == "m":
                if self.param not in ("dec", "hex", "bin"):
                    return False
                self.driver.mode = self.param

        if self.action not in ALLOWED_ACTIONS:
            return False
        self.action = self.action[0]

        return True

    def get_action(self):
        while not self.input_ask():
            print(f"Unrecognized command: {self.action}")

    def handle_s(self):
        self.driver.reg_dump()
        self.driver.print_cur()
        self.get_action()

    def handle_l(self):
        if self.spread:
            spread = self.spread
        else:
            spread = 3

        self.driver.print_cur(spread=spread)
        self.spread = None
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
