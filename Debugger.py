from Driver import Driver

class Debugger():

    def __init__(self, driver):
        self.driver = driver

    def debug(self):
        self.driver.setup()
        while self.driver.active():
            inst = self.driver.cur_inst()
            if inst.b_point:
                print(inst)
                input("Press enter to continue ")
            self.driver.exe_next()