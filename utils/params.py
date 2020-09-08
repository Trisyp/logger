import json
from pathlib import Path

from utils.root_dir import root_dir

config_path = Path(f"{root_dir}/config")

with open(f"{config_path}/configs.json",encoding="UTF-8") as file:
    configs = json.load(file)

max_log_size = configs["max_log_size"]
log_level = configs["log_level"]


if __name__ == '__main__':
    print(max_log_size)