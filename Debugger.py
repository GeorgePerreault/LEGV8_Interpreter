from Driver import Driver

ALLOWED_ACTIONS = ("c", "s", "l")

class Debugger():

    def __init__(self, driver):
        self.driver = driver
        self.action = "c"
        self.modifier = None

    def input_ask(self):
        s = input("")
        if s == "":
            return True

        self.action = s
        self.modifier = None

        if s[0] == "l":
            if len(s) > 2 and s[1] == " ":
                try:
                    self.modifier = int(s[2:])
                    self.action = s[0]
                except ValueError:
                    return False

        return self.action in ALLOWED_ACTIONS

    def get_action(self):
        while not self.input_ask():
            print(f"Unrecognized command: {self.action}")

    def debug(self):
        self.driver.setup()
        inst = self.driver.cur_inst()

        while self.driver.active():
            if inst and self.action == "s":
                self.driver.reg_dump()
                self.driver.print_cur()
                self.get_action()

            if inst and self.action == "l":
                if self.modifier:
                    spread = self.modifier
                else:
                    spread = 3

                self.driver.print_cur(spread=spread)
                self.get_action()
                continue

            self.driver.exe_next()

            inst = self.driver.cur_inst()
            if inst and inst.b_point:
                self.action = "s"
