#!C:/Program Files (x86)/Python37-32/python.exe
import sqlite3,cgi
import base64
form=cgi.FieldStorage()
city=form.getvalue('city')
conn=sqlite3.connect('project.db')
#cur=conn.execute('select * from accommodation where location=? limit 10',(city,))
print ("Content-type:text/html\r\n\r\n")
print("<html><body>%s</body></html>"%city)