import os
import subprocess

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(os.path.dirname(abspath))
    os.chdir(os.path.join(dname, "lol_item_verifier"))

    subprocess.call(["python3", "item_search.py"])
