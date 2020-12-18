import pyfiglet # Use this!
import sys
import random
from time import sleep
import subprocess
import getpass

fig = True if "-f" in sys.argv else False

print(f"Loading: \"{__file__}\"")
x = 0
while x <= 100:
    sleep(random.randint(10, 20) / 100)
    string = f"\r|{x * '#' + (100 - x) * ' '}| {x}%"
    print(string, end=" ")
    rint = random.randint(1, 10)
    if x >= 90:
        x = 100
        string = f"\r|{100 * '#'}| 100%"
        print(string, end=" ")
        break
    else:
        x += rint

print()

def figlet():
    name = sys.argv[2] if len(sys.argv) > 2 else getpass.getuser()
    fig_name = subprocess.run(f"figlet {''.join(['Hello', ' ', name])}".split(" "), capture_output=True).stdout.decode("utf-8")
    print(fig_name)

if fig:
    figlet()
else:
    print(sys.argv[1]) if len(sys.argv) > 1 else print("Hello World!")



