from utils.root_dir import root_dir
import datetime
from utils.params import max_log_size
from pathlib import Path
import os
import shutil
from log_module.logger import Log
log = Log()


def merge_logs(file_path, new_file):
    k = open(new_file, 'a+')
    f = open(file_path)
    k.write(f.read()+"\n")
    k.close()


def log_to_folder(from_path, file_name, file_type=".log"):
    from_path = Path(from_path)
    folder = Path(from_path)
    cnt = 1
    src_file = from_path / (file_name + file_type)
    # src_file = Path(src_file)
    if src_file.exists():
        file_date = datetime.datetime.fromtimestamp(os.stat(src_file).st_mtime).date()
        folder = folder / str(file_date)
        os.makedirs(folder, exist_ok=True)
        shutil.move(str(src_file), str(folder))
        src_file2 = folder / (file_name + file_type)
        # new_name = folder / f"log{str(datetime.date.today())}.log"
        new_name = file_name+str(file_date)
        new_file = Path(f"{folder}/{new_name}-{cnt}" + file_type)
        if src_file2.exists():
            if new_file.exists():
                while os.path.getsize(new_file)/float(1024**2) > max_log_size:
                    cnt += 1
                    new_file = Path(f"{new_name}-{cnt}" + file_type)
                merge_logs(src_file2, new_file)
                os.remove(src_file2)
            else:
                merge_logs(src_file2, new_file)
                os.remove(src_file2)


if __name__ == '__main__':
    log_to_folder(f"{root_dir}/logs", "log")
    log_to_folder(f"{root_dir}/logs", "error")
    log.info("infos test")
    log.debug("debugs test")
    log.error("errors test")


