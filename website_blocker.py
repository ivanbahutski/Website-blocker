import time
from datetime import datetime as dt

host_path = "/etc/hosts"
redirect = '127.0.0.1'
website_list = ["www.facebook.com", "facebook.com", 'www.instagram.com', 'instagram.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) \
            < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):

        with open(host_path, 'r+') as file:
            content = file.read()
            for websites in website_list:
                if websites in content:
                    pass
                else:
                    file.write(redirect + " " + websites + "\n")
        print("Working hours...")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()  # read lines is list of lines
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")

    time.sleep(30)
