#!C:/Program Files (x86)/Python37-32/python.exe
import sqlite3,cgi
import base64,random
form = cgi.FieldStorage()
sdate=form.getvalue('Start')
u_pid=form.getvalue('abc')
#print(pid)
print ("Content-type: text/html\r\n\r\n")
print('''
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css?family=Work+Sans');
body{
font-family: 'Work Sans', sans-serif;
background: #00d2ff; 
background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff); 
background: linear-gradient(to right, #3a7bd5, #00d2ff); 
  /* Thanks to uigradients :) */
}

.card{
  background:#16181a;  border-radius:14px; max-width: 300px; display:block; margin:auto;
  padding:60px; padding-left:20px; padding-right:20px;box-shadow: 2px 10px 40px black; z-index:99;
}

.logo-card{max-width:50px; margin-bottom:15px; margin-top: -19px;}

label{display:flex; font-size:10px; color:white; opacity:.4;}

input{font-family: 'Work Sans', sans-serif;background:transparent; border:none; border-bottom:1px solid transparent; color:#dbdce0; transition: border-bottom .4s;}
input:focus{border-bottom:1px solid #1abc9c; outline:none;}

.cardnumber{display:block; font-size:20px; margin-bottom:8px; }

.name{display:block; font-size:15px; max-width: 200px; float:left; margin-bottom:15px;}

.toleft{float:left;}
.ccv{width:50px; margin-top:-5px; font-size:15px;}

.receipt{background: #dbdce0; border-radius:4px; padding:5%; padding-top:200px; max-width:600px; display:block; margin:auto; margin-top:-180px; z-index:-999; position:relative;}

.col{width:50%; float:left;}
.bought-item{background:#f5f5f5; padding:2px;}
.bought-items{margin-top:-3px;}

.cost{color:#3a7bd5;}
.seller{color: #3a7bd5;}
.description{font-size: 13px;}
.price{font-size:12px;}
.comprobe{text-align:center;}
.proceed{position:absolute; transform:translate(300px, 10px); width:50px; height:50px; border-radius:50%; background:#1abc9c; border:none;color:white; transition: box-shadow .2s, transform .4s; cursor:pointer;}
.proceed:active{outline:none; }
.proceed:focus{outline:none;box-shadow: inset 0px 0px 5px white;}
.sendicon{filter:invert(100%); padding-top:2px;}

@media (max-width: 600px){
  .proceed{transform:translate(250px, 10px);}
  .col{display:block; margin:auto; width:100%; text-align:center;}
}
</style></head>

<body>''')

conn = sqlite3.connect('final.db')
conn.execute('update packages set sdate=? where u_pid=?',(sdate,u_pid))

qf=open('current.txt', 'r+')
user_id=qf.read()

user_id=user_id.strip()
#print(user_id)
conn.commit()
cur = conn.execute('SELECT * FROM packages where u_pid=?',(u_pid,))
for i in cur:
    pid=i[0]
    #print(u_pid)
    ffid=i[1]
    cost=i[6]
    city=i[2]
    hid=i[3]
    attr=i[4]
    rid=i[5]
#print(cost)
    #print(ffid," ",city," ",hid," ",attr," ",rid," ")
#print(pid)
#print(ffid," ",city," ",hid," ",attr," ",rid," ")
addr=[ ]
name=[ ]
subcat=[]
count=0

a=attr.split(",")
for i in a:
    #print(i)
    x=int(i)
    count=count+1
    cur_attr=conn.execute('select * from attraction where id=?',(x,))
    for i in cur_attr:
        addr.append(i[0])
        name.append(i[6])
        subcat.append(i[7])
#print(addr," ",name," ",subcat," ")
#"Name:%s<br/>Address:attr_address:%s<br/>%s"

cur_ffid=conn.execute('select * from FLIGHTS where id=?',(ffid,))
for i in cur_ffid:
    flight_src=i[1]
    flight_dst=i[2]
    flight_dep_time=i[3]
    flight_arr_time=i[4]
    flight_price=i[5]
#print(flight_src," ",flight_dst," ",flight_dep_time," ",flight_arr_time)

cur_hid=conn.execute('select * from accommodation where id=?',(hid,))
for i in cur_hid:
    hotel_name=i[1]
    hotel_addr=i[3]
    hotel_stars=i[4]
    hotel_cost=i[5]

cur_rid=conn.execute('select * from amsr where id=?',(rid,))
for i in cur_rid:
    restaurant_name=i[1]
    restaurant_addr=i[3]
    restaurant_stars=i[4]
    restaurant_cost=i[5]    

#cur_cost=conn.execute('select * from packages where u_pid=?',(u_pid,))
#for i in cur_cost:
#   cost=i[7]
#  print(cost)

#print("<form><input type=button value=<-BACK onclick=history.back(-1) style=color:black;/></form>")
print("<div class=container>")
print("<form >  <input type=hidden name=a value=%s>" % user_id)
print("<input type=hidden name=b value=%s>" % u_pid)
print("<input type=hidden name=c value=%s>" % sdate)
print("<input type=hidden name=d value=%s>" % cost)
print('''  <div class="card">
    <button type=submit class="proceed" formaction=action=pkgpaymentconfirmation.py>
    <svg class="sendicon" width="24" height="24" viewBox="0 0 24 24">
  <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"></path>
</svg></button>
   <img src="https://seeklogo.com/images/V/VISA-logo-62D5B26FE1-seeklogo.com.png" class="logo-card">
 <label>Card number:</label>
 <input id="user" type="text" class="input cardnumber"  placeholder="1234 5678 9101 1121">
 <label>Name:</label>
 <input class="input name"  placeholder="Edgar Pérez">
 <label class="toleft">CCV:</label>
 <input class="input toleft ccv" placeholder="321">
  </div>
  <div class=receipt>
    <div class="col"><p>Cost:</p>
    ''')
print("<h2 class=cost>%s</h2><br>" %cost)



#conn.execute("insert into pkgpayment(username,id,cost,date) values(?,?,?,?)",(user_id,u_pid,cost,sdate))


conn.commit()
#print("<p>Name:</p> <h2 class=seller>%s</h2>" %user_name)
print(  '''</div>
    <div class="col">
      <p>Package Bought:</p>''')
print("<h3 class=cost>%s Package %s</h3>" %(city,u_pid))
print("<p class=bought-items description>Hotel:%s<br/></p>" %(hotel_name))
print("<p class=bought-items description>Flight:%s<br/></p>" %(ffid))
print("<p>ITINERARY:<br/></p>")
for i in range(count):
    print("<p class=bought-items description>Name:%s<br/>Type:%s<br/></p>" %(name[i],subcat[i]))
#print('''<p class="bought-items price">$200 (50% discount)</p><br>
#      <h3 class="bought-items">Gaming keyboard</h3>
#      <p class="bought-items description">Look mommmy, it has colors!</p>
#      <p class="bought-items price">$200 (50% discount)</p><br>'''
print('''</div>
    <p class="comprobe">This information will be sended to your email</p>
  </div>
</div>

</body></html>''')
