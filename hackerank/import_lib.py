import sys
import importlib.util
import os

helper_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../helper.py'))
if not os.path.isfile(helper_path):
    raise FileNotFoundError(f"Could not find file at {helper_path}")

module_name = 'helper'
spec = importlib.util.spec_from_file_location(module_name, helper_path)
helper_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper_module)

