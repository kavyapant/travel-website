#!C:/Program Files (x86)/Python37-32/python.exe
import sqlite3,cgi
print ("Content-type:text/html\r\n\r\n")
conn=sqlite3.connect('final.db')
form=cgi.FieldStorage()
fid=form.getvalue('flight_id')
uid=form.getvalue('uid')
date=form.getvalue('date')
cost=form.getvalue('cost')
name=form.getvalue('name')
cardno=form.getvalue('cardno')
cvv=form.getvalue('cvv')
if name==None or cardno==None or cvv==None:
    page='''<html>
                        <body onload="op()">
                            <script>
                                function op(){
                                    alert('Enter valid details');
                                    history.go(-1);
                                }
                            </script>
                        </body>
                    </html>'''
    print(page)
else:
    conn.execute('insert into flightpayment values(?,?,?,?)',(uid,fid,cost,date))
    conn.commit()
    page='''<html>
                        <body onload="op()">
                            <script>
                                function op(){
                                    alert('Payment Successful');
                                    window.open('/../a.html','_self');
                                }
                            </script>
                        </body>
                    </html>'''
    print(page)  