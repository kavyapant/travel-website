#!C:/Program Files (x86)/Python37-32/python.exe
import cgi,sqlite3
form=cgi.FieldStorage()
uname=form.getvalue('username')
pword=form.getvalue('password')
print ("Content-type:text/html\r\n\r\n")
#print("<html>")
#print("<body align=center>")
flag=0
conn=sqlite3.connect('project.db')
cur=conn.execute('select * from users where username=?',(uname,))
for i in cur:
    if i:
        if i[2]==pword:
            
           # print("<h1 align=center>Login Successful<h1>")
           # print("<form action=/a.html><input type=submit  value=\"Click here to go to main page\"></form>")
            page='''<html>
                        <body onload="op()">
                            <script>
                                function op(){
                                    window.open('/../a.html');
                                }
                            </script>
                        </body>
                    </html>'''
            print(page)
            flag=1
if flag==0:
        print('''<html><body align=center>
        <h1>Login Unsuccessful<h1>
        <form action=/login.html><input type=submit value=\"Click here to go back to login page\"></form></body></html>''')