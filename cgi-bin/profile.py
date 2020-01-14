#!C:/Program Files (x86)/Python37-32/python.exe
import sqlite3,cgi
print ("Content-type:text/html\r\n\r\n")
conn=sqlite3.connect('final.db')
f=open('current.txt','r')
n=f.read().strip()
cur=conn.execute('select * from users where username=?',(n,))
cur=cur.fetchone()
print('''<html><head>
<style>
    body{
        font-face:"Times New Roman";
        font-size:24px;}
    td,th,caption{
        font-size:24px;}
</style></head>
<body>''')
print("<h1 align=center>%s</h1><br/><br/>"%(cur[1]))
print("<p><b>Username: </b>%s</p>"%(n))
print('''<p align=center>Past Bookings</p>
<table border=1 align=center cellpadding=10>
<tr><th>Sr No.</th><th>Name</th><th>Cost</th><th>Booking for</th><th>Booking Date</th>''')
cur=conn.execute('select * from hotelpayment where username=?',(n,))
col=1
for i in cur:
    cur1=conn.execute('select * from accommodation where id=?',(i[1],))
    cur1=cur1.fetchone()
    print("<tr><th>%s</th><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(col,cur1[1],i[2],"Hotel",i[3]))
    col=col+1
cur=conn.execute('select * from flightpayment where username=?',(n,))
for i in cur:
    cur1=conn.execute('select * from flights where id=?',(i[1],))
    cur1=cur1.fetchone()
    print("<tr><th>%s</th><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(col,cur1[0],i[2],"Flight",i[3]))
    col=col+1
print('''</table>
<input type=button value="Back to Homepage" onclick=history.go(-1);>
</body></html>''')
