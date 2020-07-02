#!python
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("content-type: text/html")
print()

import cgi
form = cgi.FieldStorage()
username = form["username"].value
useraddress = form["useraddress"].value
userpassword = form["userpassword"].value
usernumber = form["usernumber"].value

print(username, useraddress, userpassword, usernumber)
