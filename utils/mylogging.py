import logging
import sys
from enum import Enum

class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO

def show_log(level: LogLevel):
    logging.basicConfig(stream=sys.stdout, level=level.value)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

def log(message, level: LogLevel = LogLevel.INFO):
    logging.log(level.value, message)