import json
import os
from datetime import datetime

def load(path: str, file_type: str):
    """
    This function can load file
    File type supported :
        - JSON
    """
    if os.path.exists(path):
        if file_type == "json":
            try:
                with open(path, "r") as f:
                    data = json.load(f)
                return data
            except Exception as e:
                raise FileNotFoundError(e)
        else:
            raise ValueError(f"The file type '{file_type}', is not supported")
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")
    
def get_date_hours(style="default"):
    if style == "default":
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date
    if style == "file":
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d-%H-%M-%S")
        return formatted_date