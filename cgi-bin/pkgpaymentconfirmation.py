#!C:/Program Files (x86)/Python37-32/python.exe
import sqlite3,cgi
print ("Content-type:text/html\r\n\r\n")
conn=sqlite3.connect('final.db')
form=cgi.FieldStorage()
cardno=form.getvalue('cardno')
name=form.getvalue('name')
cvv=form.getvalue('cvv')
ids=form.getvalue('b')
uid=form.getvalue('a')
date=form.getvalue('c')
cost=form.getvalue('d')
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
    conn.execute('insert into pkgpayment values(?,?,?,?)',(uid,ids,cost,date))
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
