import psutil
import time
from backend.slv_systemes.utils.utils import load, push_value, save

def start():
    seconds = 0
    minutes = 0
    hours = 0
    while True:
        time.sleep(1)

        memory = psutil.virtual_memory()

        data = load("backend\slv_systemes\monitoring\monitoring.json", "json")
        
        seconds += 1

        if seconds == 60 or seconds > 60:
            seconds = 0
            minutes += 1

            new_data = push_value(data["ram"]["utilisation"]["last_10min_used_per_cent"], memory.percent)

        if minutes == 60 or minutes > 60:
            minutes = 0 
            hours += 1 
            new_data = push_value(data["ram"]["utilisation"]["last_10h_used_per_cent"], memory.percent)

        print(f"Fonctionnement : {hours}h {minutes}m {seconds}s")

        
        new_data = push_value(data["ram"]["utilisation"]["last_10s_used_per_cent"], memory.percent)

        data["ram"]["utilisation"]["last_10s_used_per_cent"] = new_data
        data["ram"]["total_gb"] = round(memory.total / (1024 ** 3), 1)
        data["ram"]["now_free_gb"] = round(memory.free / (1024 ** 3), 1)
        data["ram"]["now_use_gb"] = round(memory.used / (1024 ** 3), 1)

        save("backend\slv_systemes\monitoring\monitoring.json", "json", data)

        



start()
