import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("path", type=Path)
args = parser.parse_args()
root_dir = args.path


if __name__ == '__main__':
    print(root_dir)
