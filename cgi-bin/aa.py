#!C:/Program Files (x86)/Python37-32/python.exe
import sqlite3,cgi
import base64,random
form=cgi.FieldStorage()
city=form.getvalue('city')
#]data_uri = base64.b64encode(open('hotelimages/background.jpg', 'rb').read()).decode('utf-8')
#img_tag = '<img src="data:image/jpg;base64,{0}">'.format(data_uri)
conn=sqlite3.connect('final.db')
cur=conn.execute('select * from accommodation where location=?',(city,))
print ("Content-type:text/html\r\n\r\n")
co=1

print('''<html>
<head>
<style>
    h1 {
        position: relative;
        font-size: 70px;
        margin-top: 0;
        font-family: 'Times New Roman', helvetica, arial;
        color:green;
        text-decoration:underline;
    }

th{color:green;font-size:24px;}
.b{border-bottom:1px solid black;}
td{font-size:20px;}
.button {
  position: relative;
  background-color: #4CAF50;
  border: none;
  font-size: 20px;
  color: #FFFFFF;
  padding: 20px;
  width: 100px;
  text-align: center;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  text-decoration: none;
  overflow: hidden;
  cursor: pointer;
}

.button:after {
  content: "";
  background: #90EE90;
  display: block;
  position: absolute;
  padding-top: 300%;
  padding-left: 350%;
  margin-left: -20px!important;
  margin-top: -120%;
  opacity: 0;
  transition: all 0.8s
}

.button:active:after {
  padding: 0;
  margin: 0;
  opacity: 1;
  transition: 0s
}
</style></head><body>''')
k=1
print("<h1 align=center>Hotels in %s</h1>"%(city))
print("Filter:<form action=aa1.py><input type=hidden name=abc value=%s>"%(city))
print('''<select name=filter><option value=cost>cost</option><option value=stars>Rating</option></select>
<select name=order><option value=desc>Descending</option><option value=asc>Ascending</option></select>
<input type=submit value=submit></form>''')
print("<table frame=box width=100% >")
for i in cur:
    print("<tr class=b ><th rowspan=4 >%s</th><td rowspan=4>"%co)
    co=co+1       
    data_uri = base64.b64encode(open('hotelimages/'+str(k)+'.jpg', 'rb').read()).decode('utf-8')
    img_tag = '<img src="data:image/jpg;base64,{0}">'.format(data_uri)
    print(img_tag)
    print("</td><th>")
    print("%s </th></tr><tr>" % (i[1]))
    print("<td>Cost: &#8377 %s</td>"%i[5])
    print("<td rowspan=2><form action=/hotels/hotels.html>")
    print("<input type=Submit class=button value=View name=%s></form></td>"%(i[0]))
    print('</tr><tr><td >Address: %s </td></tr>' %(i[3]))
    print('<tr><td class=b>Rating :%s Stars</td></tr>' %(i[4]))
    k=(k+1)
    if k==11:
        k=1
print('''</table>

<button class=".button"  onclick=history.go(-1);>Back to Homepage</button>
</body>
</html>''')
