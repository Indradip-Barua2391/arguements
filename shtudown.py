import os

shutdown = input("do you wish to shut down your pc? (yes or no): ")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")