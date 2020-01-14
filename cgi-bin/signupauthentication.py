#!C:/Program Files (x86)/Python37-32/python.exe
import cgi,sqlite3
form=cgi.FieldStorage()
uname=form.getvalue('username')
pword=form.getvalue('password')
name=form.getvalue('name')
print ("Content-type:text/html\r\n\r\n")
if uname==None or pword==None or name==None:
    page='''<html>
                        <body onload="op()">
                            <script>
                                function op(){
                                    alert('Enter valid details');
                                    window.open('/../signup.html','_self');
                                }
                            </script>
                        </body>
                    </html>'''
    print(page)
else:
    flag=0
    conn=sqlite3.connect('final.db')
    cur=conn.execute('select * from users where username=?',(uname,))
    for i in cur:
        if i:
            if i[0]==uname:
                page='''<html>
                            <body onload="op()">
                                <script>
                                    function op(){
                                        alert('Username already exists');
                                        window.open('/../signup.html','_self');
                                    }
                                </script>
                            </body>
                        </html>'''
                print(page)
                flag=1
    if flag==0:
        conn.execute('insert into users values(?,?,?,"User")',(uname,name,pword))
        conn.commit()
        page='''<html>
                            <body onload="op()">
                                <script>
                                    function op(){
                                        alert('signup complete');
                                        window.open('/../login.html','_self');
                                    }
                                </script>
                            </body>
                        </html>'''
        print(page)
