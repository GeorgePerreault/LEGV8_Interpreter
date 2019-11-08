class LEGError(Exception):
    pass

class TokenError(LEGError):
    pass

class ParserError(LEGError):
    pass

class DebugCommandError(LEGError):
    pass

class ExecutionError(LEGError):
    pass