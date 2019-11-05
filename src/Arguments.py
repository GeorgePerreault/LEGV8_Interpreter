class Arguments:

    def __init__(self, args):
        self.file = ""
        self.mode = "dec"
        self.debug = False

        if len(args) < 2:
            print("Improper usage. Please pass a file to run.")
            exit()

        self.file = args[1]

        if "-ndec" in args:
            self.mode = "ndec"
        elif "-hex" in args:
            self.mode = "hex"
        elif "-bin" in args:
            self.mode = "bin"

        if "-d" in args:
            self.debug = True