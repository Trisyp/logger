from pathlib import Path
import json

from log_module.log_subarea import log_to_folder
from utils.root_dir import root_dir
from log_module.logger import Log
log = Log()
data_path = Path(f"{root_dir}/data")


def read_txt_file(file_name):
    log_to_folder(f"{root_dir}/logs", "log")
    log_to_folder(f"{root_dir}/logs", "error")
    try:
        with open(file_name, encoding="UTF-8") as file:
            js_data = json.load(file)
        log.info("json data has read successfully")
    except Exception as e:
        log.error(e.__str__())
    return js_data


if __name__ == '__main__':
    data = read_txt_file(f"{data_path}/exam.json")
    print(data["name"])
