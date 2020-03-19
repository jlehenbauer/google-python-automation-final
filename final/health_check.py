#! /usr/bin/env python3

import psutil
import shutil
import emails
import requests

def check_cpu():
 usage = psutil.cpu_percent(1)
 cpu_usage = [usage * 100, (1-usage) * 100]
 print(cpu_usage)
 return usage < 80

def check_disk_space():
 du = shutil.disk_usage('/')
 free = du.free / du.total * 100
 print(free)
 return free > 20

def check_memory():
 usage = psutil.virtual_memory()
 print(usage[1] >> 20)
 usage = usage[1] >> 20
 return usage > 500

def check_localhost():
 host = "http://127.0.0.1"
 r = requests.get(host)
 return r.status_code == 200

if __name__ == "__main__":
 e_m = ""
 if not check_cpu():
  e_m = "CPU usage is over 80%"
 if not check_disk_space():
  e_m = "Available disk space is less than 20%"
 if not check_memory():
  e_m = "Available memory is less than 500MB"
 if not check_localhost():
  e_m = "localhost cannot be resolved to 127.0.0.1"

 print(e_m)

 if e_m != "":
  sender = "automation@example.com"
  recipient = "student-04-a4b37efcea50@example.com"
  subject = "Error - " + e_m
  body = "Please check your system and resolve the issue as soon as possible."

  email = emails.generate_email(sender, recipient, subject, body, "")
  emails.send_email(email)
