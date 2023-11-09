import os
import csv
import subprocess


subprocess.call('runas /user:"COMPUTER-NAME\ADMIN-USER" "C:\windows\system32\cmd.exe' , shell=True)


os.system('notepad')

https://stackoverflow.com/questions/15761489/python-respond-to-command-line-prompts