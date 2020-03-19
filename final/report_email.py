#! /usr/bin/env python3

import os
import datetime
import reports
import emails

today = datetime.date.today()
today = today.strftime("%A") + " " + today.strftime("%d") + ", " + today.strftime("%Y")
filepath = os.path.expanduser("~/supplier-data/descriptions/")


if __name__ == "__main__":
 title = "Processed Update on " + today
 paragraph = ""
 for file in os.listdir(filepath):
  with open(filepath + file) as item:
   #print(item.readline())
   #print(item.readline())
   paragraph += "name: " + item.readline().rstrip() + "<br/>"
   paragraph += "weight: " + item.readline().rstrip() + "<br/><br/>"
 new_file = "/tmp/processed.pdf"

 print(paragraph)
 reports.generate_report(new_file, title, paragraph)

 sender = "automation@example.com"
 recipient = "student-04-a4b37efcea50@example.com"
 subject = "Upload Completed - Online Fruit Store"
 body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
 attachment = new_file
 new_email = emails.generate_email(sender, recipient, subject, body, attachment)
 emails.send_email(new_email)
