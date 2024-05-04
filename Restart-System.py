import os
import platform

osv = platform.system()
print(osv)

class restart(osv):

    if osv == "Windows":
        os.system("shutdown /r /t 1")

    elif osv == "Linux" or osv == "Unix":
        os.system("sudo reboot -r now")

    elif osv == "macOS":
        os.system("sudo su -r now")