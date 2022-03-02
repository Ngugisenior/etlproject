import os
from datetime import datetime

# Git Commit
cmd = f"git add . && git commit -m '{datetime.now()}'"
os.system(cmd)
