from colorama import Fore, Back, Style, init
from datetime import datetime
from backend.slv_systemes.utils.utils import get_date_hours, load

class Logger:
    def __init__(self, log_conf_file:str, style={"debug":Fore.BLUE, "info":Fore.GREEN, "warn":Fore.YELLOW, "error":Fore.RED}, log_levels=3):
        """
        Initializes the style and default prefixes,  
        loads the settings, and creates a new log file.
        """

        self.style = style

        self.prefix_debug = "DEBUG"
        self.prefix_info = "INFO"
        self.prefix_warn = "WARN"
        self.prefix_error = "ERROR"

        self.log_level = log_levels

        self.log_settings = load(log_conf_file, "json")

        if self.log_settings is not None:
            if "on_file" in self.log_settings:
                self.set_on_file = bool(self.log_settings["on_file"])
            else:
                self.set_on_file = False

            if "on_console" in self.log_settings:
                self.set_on_console = bool(self.log_settings["on_console"])
            else:
                self.set_on_console = False

        self.logs_files_path = self.log_settings["on_file_config"]["file_path"]

        self.new_file_logs_name = get_date_hours("file")

        with open(f"{self.logs_files_path}/{self.new_file_logs_name}.log", "a") as log_file:
            log_file.write(f"========== Log file of {self.new_file_logs_name} ========== \n")

    def create_prefix(self, levels, log_type, date_style=None, prefix_style="default"):
        """
        Creates a prefix based on the log configuration.
        Two possibilities:
        - Console prefixes
        - File prefixes
        """

        if date_style is None:
            if log_type == "console":
                date_style = self.log_settings["on_console_config"]["date_style"]
            else:
                prefix_style = self.log_settings["on_file_config"]["date_style"]

        if prefix_style is None:
            if log_type == "console":
                prefix_style = self.log_settings["on_console_config"]["prefix_style"]
            else:
                prefix_style = self.log_settings["on_file_config"]["prefix_style"]

        if log_type == "console":
            if levels == "debug":
                now = get_date_hours(date_style)
                if prefix_style == "default":
                    return f"[{now} - {self.prefix_debug}] "
                
            if levels == "info":
                now = get_date_hours(date_style)
                if prefix_style == "default":
                    return f"[{now} - {self.prefix_info}] "
                
            if levels == "warn":
                now = get_date_hours(date_style)
                if prefix_style == "default":
                    return f"[{now} - {self.prefix_warn}] "
                
            if levels == "error":
                now = get_date_hours(date_style)
                if prefix_style == "default":
                    return f"[{now} - {self.prefix_error}] "
        else:
            if levels == "debug":
                now = get_date_hours("file")
                return f"{now} {self.prefix_debug}"
                
            if levels == "info":
                now = get_date_hours("file")
                return f"{now} {self.prefix_info}"
                
            if levels == "warn":
                now = get_date_hours("file")
                return f"{now} {self.prefix_warn}"
                
            if levels == "error":
                now = get_date_hours("file")
                return f"{now} {self.prefix_error}"

    def write_log(self, log):
        """
        Write in the file of logs.
        """
        with open(f"{self.logs_files_path}/{self.new_file_logs_name}.log", "a") as log_file:
            log_file.write(log)

    def debug(self, message: str):
        if self.log_level == 4 or self.log_level > 4:
            if self.set_on_console == True:
                prefix = self.create_prefix("debug", log_type="console")
                print(self.style["debug"] + prefix + message + Fore.RESET)
            if self.set_on_file == True:
                prefix = self.create_prefix("debug", log_type="file")
                self.write_log(log=f"{prefix} {message}\n")
        else:
            pass

    def info(self, message: str):
        if self.set_on_console == True:
            prefix = self.create_prefix("info", log_type="console")
            print(self.style["info"] + prefix + message + Fore.RESET)
        if self.set_on_file == True:
            prefix = self.create_prefix("info", log_type="file")
            self.write_log(log=f"{prefix} {message}\n")

    def warn(self, message: str):
        if self.set_on_console == True:
            prefix = self.create_prefix("warn", log_type="console")
            print(self.style["warn"] + prefix + message + Fore.RESET)
        if self.set_on_file == True:
            prefix = self.create_prefix("warn", log_type="file")
            self.write_log(log=f"{prefix} {message}\n")

    def error(self, message: str):
        if self.set_on_console == True:
            prefix = self.create_prefix("error", log_type="console")
            print(self.style["error"] + prefix + message + Fore.RESET)
        if self.set_on_file == True:
            prefix = self.create_prefix("error", log_type="file")
            self.write_log(log=f"{prefix} {message}\n")