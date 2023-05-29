import datetime
import time

#to run, open cmd prompt as admin -> go to this project repo -> run the command "python main.py"

end_time = datetime.datetime(2023,5,28)
site_block = ["www.docker.com","www.facebook.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now()<end_time:
        print("Start Blocking")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect + " " + website + "\n")
                else:
                    pass
    else:   #Website will be unblocked when current time > end time
        with open(host_path, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0) #put the pointer at the starting of host file
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate()
        time.sleep(5)


