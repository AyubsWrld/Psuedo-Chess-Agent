from enum import Enum

class LogLevel(Enum):
    INFO = 1
    DEBUG = 2
    WARN = 3
    ERROR = 4

def log(level: LogLevel, message: str):
    colors = {
        LogLevel.INFO: "\033[32m[INFO]\033[0m",
        LogLevel.DEBUG: "\033[36m[DEBUG]\033[0m",
        LogLevel.WARN: "\033[33m[WARN]\033[0m",
        LogLevel.ERROR: "\033[31m[ERROR]\033[0m",
    }
    
    print(colors.get(level, "\033[37m[UNKNOWN]\033[0m"), message)
