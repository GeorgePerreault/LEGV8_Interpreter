class DebugCommandError(Exception):
    pass

class DebugCommandParser:

    def __init__(self):
        self.ALLOWED_ACTIONS = ("continue", "step", "list", "mode", "c", "s", "l", "m")


    def parse_command(self, s):        
        s = s.split()

        action = s[0]
        param = s[1] if len(s) == 2 else None
        mode = None
        spread = None

        if action not in self.ALLOWED_ACTIONS:
            raise DebugCommandError(f"Invalid command: {action}")
        action = action[0]

        if not param:
            return action, mode, spread

        if action[0] == "l":
            try:
                spread = int(param)
            except ValueError:
                raise DebugCommandError(f"Invalid parameter for command list: {param}")
        elif action[0] == "m":
            if param not in ("ndec", "dec", "hex", "bin"):
                raise DebugCommandError(f"Invalid parameter for command mode: {param}")
            mode = param

        return action, mode, spread