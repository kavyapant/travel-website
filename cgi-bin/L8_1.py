#!C:/Program Files (x86)/Python37-32/python.exe
import os
print ("Content-type: text/html\r\n\r\n")
print ("<font size=+1>Environment</font><br/>")
for param in os.environ.keys():
	print ("<b>%s</b>: %s<br/>" % (param, os.environ[param]))

