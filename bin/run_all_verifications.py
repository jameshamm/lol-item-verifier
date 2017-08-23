import os
import subprocess

abspath = os.path.abspath(__file__)
dname = os.path.dirname(os.path.dirname(abspath))
os.chdir(os.path.join(dname, "lol_item_verifier"))

subprocess.call(["python3", "main.py"])
# subprocess.call(["python3", "playing_tests.py"])
