#!C:/Program Files (x86)/Python37-32/python.exe
import cgi
form=cgi.FieldStorage()
username=form.getvalue('username')
password=form.getvalue('password')
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<body>")
print ("<h2>Hello %s %s</h2>" % (username, password))
print ("</body>")
print ("</html>")

