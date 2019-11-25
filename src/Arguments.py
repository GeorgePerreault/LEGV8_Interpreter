class Arguments:
    # This class parses the arguments passed to the program on run

    def __init__(self, args):
        self.file = ""
        self.mode = "dec"
        self.debug = False

        if len(args) < 2:
            print("Improper usage. Please pass a file to run.")
            exit()

        self.file = args[1]

        for mode in {"dec", "udec", "hex", "bin"}:
            if f"-{mode}" in args:
                self.mode = mode

        if "-d" in args:
            self.debug = True

        if "-help" in args:
            print("Please see the README, I'm too lazy to restate it here")
            exit()