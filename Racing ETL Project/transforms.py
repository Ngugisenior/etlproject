from dataclasses import dataclass
import os
from commit import cmd
from datetime import datetime

def parse_dates(_date):
    return datetime.strptime(_date, "%Y-%M-%d").date()


os.system(cmd)