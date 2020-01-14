#!C:/Program Files (x86)/Python37-32/python.exe
# Import modules for CGI handling 
import cgi
import base64
import pandas as pd
import sqlite3,random
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
city = form.getvalue('city')
conn = sqlite3.connect('final.db')
cur = conn.execute('SELECT * FROM attraction where location=? order by subCategory asc',(city,))

print ("Content-type:text/html\r\n\r\n")
co=1
print('''<html>
<head>
<style>
th{color:green;font-size:24px;}
.b{border-bottom:1px solid black;}
td{font-size:20px;}
</style></head><body>''')
k=1
print("<h1 align=center>Attractions in %s</h1>" %(city))
print("<table frame='box' width=100% >")
for i in cur:
    print("<tr class=b ><th rowspan=3 >%s</th><td rowspan=3>"%co)
    co=co+1    
    data_uri = base64.b64encode(open('arrange/arrange-'+str(k)+'.jpg', 'rb').read()).decode('utf-8')
    img_tag = '<img src="data:image/jpg;base64,{0}">'.format(data_uri)
    print(img_tag)
    k=k+1
    if (k==10):
        k=1

    print("</td><th>")
    print("%s</th></tr><tr>" % (i[7]))
    print("<td>Name:%s</td>"%i[6])
    #print("<td rowspan=2><form action=/ggg.html>")
    #print("<input type=Submit value=Book name=%s></form></td>"%(i[2]))
    print('</tr><tr class=b><td class=b> %s </td></tr>' %(i[0]))

   
print('''</table>

<form><input type=button value="Back" onclick=history.go(-1);>
</form>
</body>
</html>''')
