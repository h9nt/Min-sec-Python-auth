import psutil
import threading
import subprocess
import base64
import requests


class Antidebug:  # Credits goes to xTekky for the AntiDebug!
    def __init__(self) -> None:
        pass

    def _exit(self):
        return True

    def process_check(self):
        while True:
            PROCESSES = [
                "http toolkit.exe",
                "httpdebuggerui.exe",
                "wireshark.exe",
                "fiddler.exe",
                "charles.exe",
                "regedit.exe",
                "cmd.exe",
                "taskmgr.exe",
                "vboxservice.exe",
                "df5serv.exe",
                "processhacker.exe",
                "vboxtray.exe",
                "vmtoolsd.exe",
                "vmwaretray.exe",
                "ida64.exe",
                "ollydbg.exe",
                "pestudio.exe",
                "vmwareuser",
                "vgauthservice.exe",
                "vmacthlp.exe",
                "x96dbg.exe",
                "vmsrvc.exe",
                "x32dbg.exe",
                "vmusrvc.exe",
                "prl_cc.exe",
                "prl_tools.exe",
                "qemu-ga.exe",
                "joeboxcontrol.exe",
                "ksdumperclient.exe",
                "ksdumper.exe",
                "joeboxserver.exe",
                "xenservice.exe",
            ]
            for proc in psutil.process_iter():
                if any(procstr in proc.name().lower() for procstr in PROCESSES):
                    try:
                        proc.kill()
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass

    def __main__(self):
        try:
            threading.Thread(target=self.process_check).start()
            return False
        except:
            return False

    def check(self):
        if Antidebug().__main__():
            print("Program failed to execute")
        else:
            print("success")


class SmAuth:
    @staticmethod
    def xor(string, key):
        result = b""
        key_len = len(key)
        for i in range(len(string)):
            result += bytes([ord(string[i]) ^ ord(key[i % key_len])])
        return base64.b64encode(result).decode()
    
    @staticmethod
    def auth() -> str: # Its no Ultimate Auth improve it if needed.
        try:
            hwid = SmAuth().xor(
                subprocess.check_output("wmic csproduct get uuid")
                .decode()
                .split("\n")[1]
                .strip(),
                "", # Your secret key from the backend , must be the same!
            )
            url = ""  # ur url
        
            payload = "hwid={}".format(hwid)
        
            headers = {
                "Content-Type"  : "application/x-www-form-urlencoded",
                "Connection"    : "keep-alive",
                "User-Agent"    : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
            }
            response = requests.post(url, headers=headers, data=payload).json()
        
            if 'status' in response and response["status"] != True:
                return False
            else:
                return True
        except Exception as e:
            return {"error": str(e)}
