import sys
from datetime import datetime

start_time = datetime.now()

class Logger:
    __verbose = sys.argv.count("--verbose") > 0

    @staticmethod
    def __log(message: str, prefix: str | None = None):
        if Logger.__verbose:
            if prefix is None:
                print(message)
            else:
                print(f"[{prefix}] {message} ({round((datetime.now() - start_time).total_seconds(), 3)}s)")

    @staticmethod
    def log_info(message: str):
        Logger.__log(message, "INFO")

    @staticmethod
    def log_error(message: str):
        Logger.__log(message, "ERROR")

    @staticmethod
    def log_warning(message: str):
        Logger.__log(message, "WARNING")
