#!C:/Program Files (x86)/Python37-32/python.exe
import sqlite3,cgi,cgitb
cgitb.enable()
import base64,random
form=cgi.FieldStorage()
t=form.getvalue('abc').split('=')[0]
c=form.getvalue('Check-in')
conn=sqlite3.connect('final.db')
q="select * from accommodation where id="+t
cur=conn.execute(q)
for i in cur:
    cost=i[5]
cur=conn.execute(q)
print ("Content-type:text/html\r\n\r\n")
f=open('current.txt','r')
n=f.read()
print('''<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css?family=Work+Sans');
body{
font-family: 'Work Sans', sans-serif;
background: #00d2ff; 
background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff); 
background: linear-gradient(to right, #3a7bd5, #00d2ff); 
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
</style></head><body>
<div class="container">
  <div class="card">
    <form action=paymentconfirmation.py>
    <button type=submit class="proceed" ><svg class="sendicon" width="24" height="24" viewBox="0 0 24 24">
  <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"></path>
</svg></button>
   <img src="https://seeklogo.com/images/V/VISA-logo-62D5B26FE1-seeklogo.com.png" class="logo-card">
 <label>Card number:</label>
 <input  class="input cardnumber" name="cardno" id="user"  placeholder="1234 5678 9101 1121">
 <label>Name:</label>
 <input class="input name"  placeholder="Name" name="name">
 <label class="toleft">CCV:</label>
 <input class="input toleft ccv" placeholder="CVV" name="cvv">''')
print("<input type=hidden name=hid value=%s>"%(t))
print("<input type=hidden name=\"date\" value=\"%s\">"%(c))
print("<input type=hidden name=cost value=%s>"%(cost))
print("<input type=hidden name=uid value=%s></form>"%(n.strip()))
print(''' </div>
  <div class="receipt">
    <div class="col"><p>Cost:</p>''')
for i in cur:
    print("<h2 class=cost>&#8377 %s</h2><br>"%(i[5]))

    r="select * from users where username=\""+n.strip()+"\""
    a=conn.execute(r)
    for j in a:
        print("<p>Name:</p><h2 class=seller>%s</h2>"%(j[1]))
    print('''
    </div>
    <div class="col">
      <p>Payment for booking hotel:</p>''')
    print("<h3 class=seller>%s</h3>"%(i[1]))
    print("<p>Location:</p><h2 class=seller> %s</h2>"%(i[2]))
    print("<p>Booking date:</p><h2 class=seller>%s</h2><br/>"%(c))
    print('''
    </div>
    <p class="comprobe">This information will be sended to your email</p>
    </div>
  
</div>
</body></html>''')
