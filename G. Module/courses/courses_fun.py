
"""
to import custom module in python
---------------------------------
import os, sys [operating system, system]
from os.path import dirname, join, abspath
sys.path.insert(0,abspath(join(dirname(__file__), "..")))
"""

import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0,abspath(join(dirname(__file__), "..")))

from payments import payments_fun

def course():
    print("Course deatils")

payments_fun.payments()