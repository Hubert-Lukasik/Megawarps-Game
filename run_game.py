import os

try:
    should_work_on_linux = os.uname()
    os.system("python3 code/main.py")
except AttributeError: #Windows
    os.system("py code/main.py")