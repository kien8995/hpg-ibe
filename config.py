import os
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

config: dict = load(open(f"{ROOT_DIR}/config.yml"), Loader=Loader)

config_str = dump(config, Dumper=Dumper)
