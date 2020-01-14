#!C:/Program Files (x86)/Python37-32/python.exe
import sqlite3,cgi
print ("Content-type:text/html\r\n\r\n")
conn=sqlite3.connect('final.db')
form=cgi.FieldStorage()
cardno=form.getvalue('cardno')
name=form.getvalue('name')
cvv=form.getvalue('cvv')
id=form.getvalue('hid')
uid=form.getvalue('uid')
date=form.getvalue('date')
cost=form.getvalue('cost')
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
    conn.execute('insert into hotelpayment values(?,?,?,?)',(uid,id,cost,date))
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