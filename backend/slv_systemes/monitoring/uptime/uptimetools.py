from backend.slv_systemes.monitoring.uptime.uptime import start_uptime
from backend.slv_systemes.utils.utils import load, push_value, save, get_date_hours

class Uptime:
    def __init__(self, uptime_file_path="backend/config/uptime.json"):
        self.path_file = uptime_file_path

    def start(self):
        start_uptime()

    def get_uptime(self, when="all_time"):
        data = load(self.path_file, "json")

        if when == "all_time":
            return data["all_time"]["up_time_percent"]
