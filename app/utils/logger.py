from __future__ import annotations

from datetime import datetime


class FileOrDirectoryNotExistingException(Exception):
    pass


class Logger:
    def __init__(self, log_dir: str = "./logs/"):
        self.log_dir = log_dir

    def log(self, msg: str, type: str = "INFO", write_to_log_file: bool = True) -> str:
        """
        Log simply logs a message to the console


        :param msg:
        :type msg:
        :param type:
        :type type:
        :return:
        :rtype:
        """
        line = f"[{datetime.now()}] [{type.upper()}] {msg}"
        print(line)
        if write_to_log_file:
            self.write_line_to_file(type, line)
        return line

    def write_line_to_file(self, filename: str, line: str) -> None:
        try:
            with open(f"{self.log_dir}{filename}", "a") as f:
                f.write(line + "\n")

        except:
            raise FileOrDirectoryNotExistingException
