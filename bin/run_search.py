import os
import subprocess
import sys

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(os.path.dirname(abspath))
    os.chdir(os.path.join(dname, "lol_item_verifier"))

    # The first item in sys.argv is the script name
    subprocess.call(["python3", "item_search.py"] + sys.argv[1:])
