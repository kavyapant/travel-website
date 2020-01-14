#!C:/Program Files (x86)/Python37-32/python.exe
import cgi,sqlite3
form=cgi.FieldStorage()
t=form.getvalue('abc').split('=')[0]
conn=sqlite3.connect('project.db')
#q="select * from accommodation where name like \'%"+t+"%\'"
q="select * from accommodation where id="+t
cur=conn.execute(q)
print ("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<br/>")
for i in cur:
    print("%s %s %s %s %s<br/>" % (i[0],i[1],i[2],i[3],i[4]))
print("</body></html>")
