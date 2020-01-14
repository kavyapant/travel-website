#!C:/Program Files (x86)/Python37-32/python.exe
import cgi,sqlite3
form=cgi.FieldStorage()
uname=form.getvalue('username')
pword=form.getvalue('password')
#type=form.getvalue('name')
print ("Content-type:text/html\r\n\r\n")
#print("<html>")
#print("<body align=center>")
flag=0
conn=sqlite3.connect('final.db')
cur=conn.execute('select * from users where username=?',(uname,))
for i in cur:
    if i:
        if i[2]==pword:
            f=open('current.txt','w+')
            f.write(i[0])
            f.close()
            page='''<html>
                        <body onload="op()">
                            <script>
                                function op(){
                                    alert('Login Successful');
                                    window.open('/../a.html','_self');
                                }
                            </script>
                        </body>
                    </html>'''
            print(page)
            flag=1
if flag==0:
    page='''<html>
                        <body onload="op()">
                            <script>
                                function op(){
                                    alert('Login Unsuccessful');
                                    window.open('/../login.html','_self');
                                }
                            </script>
                        </body>
                    </html>'''
    print(page)