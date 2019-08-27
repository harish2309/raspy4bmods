import subprocess
import re
import os
import time
cnt=1

def check_output(command_list):
    proc = subprocess.Popen(command_list, stdout=subprocess.PIPE)
    proc.wait()
    return proc.stdout.read()

while(1):
    cmds=check_output(["apcaccess","status"])
    valz=cmds.decode('utf-8')
    #print(valz)
    batz=re.findall(r'LINEV\s+:\s(\d\d\d)',valz)
    if not bool(batz):
        theone=0
        print("FAILURE ALERT WE ARE AT "+str(theone)+" volts")
        cnt=cnt+1
    else:
        theone=int("".join(map(str,batz)))
        print("The Voltage is at "+str(theone)+" volts")
        
    if cnt > 5:
        os.system('shutdown -h now')
        
    time.sleep(1)

