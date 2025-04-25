from backend.slv_systemes.utils.logger import Logger

log = Logger(log_conf_file="backend/config/logconf.json")

def debug(message):
    log.debug(message)

def info(message):
    log.info(message)

def warn(message):
    log.warn(message)

def error(message):
    log.error(message)