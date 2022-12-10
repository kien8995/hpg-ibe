"""
    app config
"""
import os
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app_config: dict = {}
with open(f"{ROOT_DIR}/application.yml", encoding="utf8") as file:
    app_config = load(file, Loader=Loader)

app_config_str = dump(app_config, Dumper=Dumper)
