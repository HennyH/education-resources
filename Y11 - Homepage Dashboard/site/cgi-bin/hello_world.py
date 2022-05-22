#!/usr/bin/env python3
import cgi
import datetime
import cgitb

cgitb.enable()

print("Content-Type: text/html")
print()
print(f"<h1>hello world it's {datetime.date.today()}</h1")