import time
from backend.slv_systemes.utils.utils import load, push_value, save, get_date_hours
import datetime

def start(uptime_path="backend/config/uptime.json"):
    data = load(uptime_path, "json")
    
    now = get_date_hours("default")

    if data["derniere_verification"] == "":
        pass
    else:
        if isinstance(data["derniere_verification"], str):
            data["derniere_verification"] = datetime.datetime.strptime(data["derniere_verification"], "%Y-%m-%d %H:%M:%S")

        if isinstance(now, str):
            now = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
        
        difference = now - data["derniere_verification"]
        data["all_time"]["down_total_s"] += difference.total_seconds()
        data["temps_derniere_coupure"] = difference.total_seconds()
        data["derniere_verification"] = now.strftime("%Y-%m-%d %H:%M:%S")

    save(uptime_path, "json", data)

    while True:
        time.sleep(1)
        data = load(uptime_path, "json")

        now = get_date_hours("default")
        data["derniere_verification"] = now
        data["all_time"]["up_total_s"] += 1

        total_time_s = data["all_time"]["up_total_s"] + data["all_time"]["down_total_s"]
        uptime_percent = (data["all_time"]["up_total_s"] / total_time_s) * 100
        data["all_time"]["up_time_percent"] = round(uptime_percent, 1)

        save(uptime_path, "json", data)
    
def start_uptime():
    start()