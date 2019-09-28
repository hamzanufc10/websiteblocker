import time
from datetime import datetime as dt
host_temp="hosts"
host_new=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website=["www.facebook.com","facebook.com","fb.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,2,45):
        print("working hours")
        with open(host_new,"r+") as file:
            content=file.read()
            for w in website:
                if w in content:
                    pass
                else:
                    file.write(redirect + " " +w+"\n")

    else:
        with open(host_new, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(w in line for w in website):
                    file.write(line)
                file.truncate()
            print("fun hours")
    time.sleep(5)




