#!C:/Users/Siddharth/AppData/Local/Programs/Python/Python37-32/python.exe
import sqlite3
import cgi
import os


flight_id=str(os.environ['QUERY_STRING'])[0:6]

form=cgi.FieldStorage()

date=form.getvalue('date')


con=sqlite3.connect('final.db')
res=con.execute('SELECT * FROM FLIGHTS WHERE ID =\''+flight_id+'\';')
res=res.fetchone()

price = res[5]
if flight_id[0:2] == 'AI':
	flight_com='AIR INDIA'
elif flight_id[0:2] == 'EY':
	flight_com='ETIHAD'
elif flight_id[0:2] == 'SG':
	flight_com='SPICE JET'
elif flight_id[0:2] == '6E':
	flight_com='INDIGO'

if res[2] == 'TXL':
	dst='Berlin'
elif res[2] == 'DXB':
	dst='Dubai'
elif res[2] == 'BCN':
	dst='Barcelona'
elif res[2] == 'AMS':
	dst='Amsterdam'
elif res[2] == 'FCO':
	dst='Rome'
elif res[2] == 'TSC':
	dst='Tuscany'
elif res[2] == 'LHR':
	dst='London'
elif res[2] == 'CDG':
	dst='Paris'

flight_desc=flight_id+'	-	'+res[1]+' to '+ dst



file=open('current.txt', 'r')
uid=file.read()
query='SELECT * FROM users WHERE username =\''+uid+'\' ;'
res=con.execute(query)
res=res.fetchone()
name=res[1]
print("Content-type:text/html\r\n\r\n")
page='''
<html>
	<head>
	<script>
            function op(){
                history.go(-1);
            }
        </script>
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
.back{
	widht: 200px;
	margin-top: 50px;
	margin-bottom: 50px;
}
.book{
	color: #fff;
	background-color: #4fa3e3;
	font-weight: 400;
	height: 45px;
	font-size: 18px;
	border: none;
	width: 15%;
	border-radius: 4px;
	text-transform: uppercase;
	float: left;
}
	</style>
	</head>
<body>
    <div class="container">
    <form action="flightpaymentconf.py" method="GET">
  <div class="card">
    <button  type="submit" class="proceed" onclick="flightpaymentconf.py"><svg class="sendicon" width="24" height="24" viewBox="0 0 24 24">
  <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"></path>
</svg></button>
   <img src="https://seeklogo.com/images/V/VISA-logo-62D5B26FE1-seeklogo.com.png" class="logo-card">
 <label>Card number:</label>
 <input id="user" type="text" class="input cardnumber"  placeholder="1234 5678 9101 1121" name="cardno">
 <label>Name:</label>
 <input class="input name"  name="name" placeholder="Edgar Pérez">
 <label class="toleft">CCV:</label>
 <input class="input toleft ccv" name="cvv" placeholder="321">
 <input type="hidden" name="uid" value="'''+uid+'''">
 <input type="hidden" name="flight_id" value="'''+flight_id+'''">
 <input type="hidden" name="date" value="'''+str(date)+'''">
 <input type="hidden" name="cost" value="'''+str(price)+'''">
  </div>
  </form>
  <div class="receipt">
    <div class="col"><p>Cost:</p>
    <h2 class="cost">Rs. '''+str(price)+'''</h2><br>
    <p>Name:</p>
    <h2 class="seller">'''+name+'''</h2>
    </div>
    <div class="col">
      <p>Flight Details:</p>
      <h3 class="cost">'''+flight_com+'''</h3><br> 	 
      <h3 class="cost">'''+flight_desc+'''</h3><br>
      <h3 class="cost">Rs. '''+str(price)+'''</h3><br>
    </div>
    <p class="comprobe">This information will be sent to your email</p>
	</div>
  </div>
</div>
</body>
</html>
'''
print(page)
