import threading
from backend.slv_systemes.utils.logger import Logger
from backend.slv_systemes.utils.utils import load
from backend.slv_systemes.api.api import api_start
from backend.slv_systemes.monitoring.ram.monitoring_ram import monitoring_ram_start
from backend.slv_systemes.monitoring.uptime.uptimetools import Uptime


config = load("backend/config/config.json", "json")

log = Logger("backend/config/logconf.json", log_levels=config["log_level"])

log.info("Starting...")

uptime = Uptime()

thread_api = threading.Thread(target=api_start)
thread_ram = threading.Thread(target=monitoring_ram_start)
thread_uptime = threading.Thread(target=uptime.start())

log.debug("API Thread is starting")
try:
    thread_api.start()
    log.debug("API Thread started successfully")
except Exception as e:
    log.error(f"API Thread encountered an error : {e}")

log.debug("Ram Monitoring Thread is starting")
try:
    thread_ram.start()
    log.debug("Ram Monitoring Thread started successfully")
except Exception as e:
    log.error(f"Ram Monitoring Thread encountered an error : {e}")

log.debug("Uptime Thread is starting")
try:
    thread_uptime.start()
    log.debug("Uptime Thread started successfully")
except Exception as e:
    log.error(f"Uptime Thread encountered an error : {e}")

log.info("System Start sucessfully !")