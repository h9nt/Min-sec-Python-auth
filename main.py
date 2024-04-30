from requests   import request
from utils      import *
import subprocess

#Antidebug().check()

print(
    f"Your Hwid >>> {subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()}"
)


if (SmAuth().auth()) != True:
    print("Not authed!")
    raise SystemExit
else:
    print("authed!")
