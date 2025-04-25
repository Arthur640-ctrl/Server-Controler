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
    
def save(path: str, file_type: str, data):

    if os.path.exists(path):
        if file_type == "json":
            try:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
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
    
def push_value(data: dict, new_value: int):
    for i in reversed(range(1, len(data))):
        data[f"{i}"] = data[f"{i - 1}"]
    
    first_key = list(data.keys())[0]
    data[first_key] = new_value
    return data
