#!C:/Users/Siddharth/AppData/Local/Programs/Python/Python37-32/python.exe
import sqlite3
import cgi

con=sqlite3.connect('final.db')

form=cgi.FieldStorage()

frm=form.getvalue('source')
dst=form.getvalue('destination')
date=form.getvalue('date')

query='SELECT* FROM FLIGHTS WHERE SRC = ? AND DST = ?;'
res=con.execute(query, (frm, dst))
flights=[]
for i in res:
	flights.append(i)


print("Content-type:text/html\r\n\r\n")
page='''
<!DOCTYPE html>
<html>
<head>
	<script>
            function op(){
                history.go(-1);
            }
        </script>
	<title>Flight Booking</title>
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
	 <style>
		body {
  			background-image: url('img/background.jpg');
  			background-size: cover;
			background-position: center;
			color: #191a1e;
		}
		.body{
	font-family: 'Montserrat', sans-serif;
	background-image: url('../img/background.jpg');
	background-size: cover;
	background-position: center;
	color: #191a1e;
}
.roundcorner{
	border-radius: 25px;
 	border: 2px solid #004040;
	padding: 20px;
	width: 1250px;
	height: 50px;
	margin-top: 100px; 
	margin-left: 25px;
	color: black;
	text-align: center;
}
.roundcorner1{
	border-radius: 25px;
 	border: 2px solid #004040;
	padding: 20px;
	width: 1250px;
	height: 50px;
	margin-top: 50px; 
	margin-left: 25px;
	color: black;
	text-align: center;
}
.roundcorner2{
	border-radius: 25px;
 	border: 2px solid #004040;
	padding: 20px;
	width: 900px;
	height: 25px;
	top: 0;
	margin-left: 350px;
	color: black;
	text-align: center;
	position: fixed;
}
.airline-name{
	position: relative;
	opacity: .6;
	font-size: 20px;
	font-weight: 600;
	width: 20%;
	color: black;
	float: left;
}
.airline-logo{
	height: 45px;
	width: 10%;
	float: left;
}
.airline-des{
	opacity: .6;
	width: 10%
	font-size: 12px;
	font-weight: 600;
	color: #4d4d4d;
}
.airline-time{
	position: relative;
	font-size: 18px;
	width: 40%;
	font-size: 1.8rem;
	color: #4a4a4a;
	float: left;
}
.airline-price{
	font-size: 18px;
	font-size: 1.8rem;
	width:15%;
	color: #4a4a4a;
	float: left;
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
.head1{
	color: #4d4d4d;
	font-size: 20px;
	float: left;
	margin-top: 50px;
	margin-left: 200px
}
.head2{
	color: #4d4d4d;
	font-size: 20px;
	float: left;
	margin-top: 50px;
	margin-left: 230px
}
.head3{
	color: #4d4d4d;
	font-size: 20px;
	float: left;
	margin-top: 50px;
	margin-left: 150px
}
.head4{
	color: #4d4d4d;
	font-size: 20px;
	float: left;
	margin-top: 50px;
	margin-left: 150px
}
.back{
	margin-left:650px;
	widht: 200px;
	margin-top: 50px;
	margin-bottom: 50px;
}
</style>
</head>
<body class="body">
	<div>
		<div style="text-align: center;">
			<h2>Flight Search Results</h2>
		</div>
		<div>
			<div class="head1">
				Airlines
			</div>
			<div class="head2">
				Departure
			</div>
			<div class="head3">
				Arrival
			</div>
			<div class="head4">
				Price
			</div>
		</div>
			<div class="roundcorner">
				<div class="airline-logo">
						<img src="https://s3-us-west-2.amazonaws.com/paytm-travel/travel_db/flights/airlines+logo/SG.png">
				</div>
				<div class="airline-name">
					SPICE JET
					<div class="airline-des">
						'''+str(flights[0][0])+''' 
					</div>
				</div>
				<div class="airline-time">
					'''+str(flights[0][3])+'''  <img src="https://d274ft55l0imju.cloudfront.net/flights/icons/srp_arrow.svg">  '''+str(flights[0][4])+''' 
				</div>
				<div class="airline-price">
					<span>&#8377;</span>'''+str(flights[0][5])+''' 
				</div>
				<div>
				<form action="/cgi-bin/payments.py" method="GET">
					<input type="hidden" name="'''+str(flights[0][0])+'''" value="get">
					<input type="hidden" name="date" value="'''+date+'''">
					<input type="submit" value="BOOK" class="book">
				</form>
				</div>
			</div>
			<div class="roundcorner1">
				<div class="airline-logo">
						<img src="https://s3-us-west-2.amazonaws.com/paytm-travel/travel_db/flights/airlines+logo/AI.png">
				</div>
				<div class="airline-name">
					AIR INDIA
					<div class="airline-des">
						'''+str(flights[1][0])+''' 
					</div>
				</div>
				<div class="airline-time">
					'''+str(flights[1][3])+''' <img src="https://d274ft55l0imju.cloudfront.net/flights/icons/srp_arrow.svg"> '''+str(flights[1][4])+''' 
				</div>
				<div class="airline-price">
					<span>&#8377;</span>'''+str(flights[1][5])+''' 
				</div>
				<div>
				<form action="/cgi-bin/payments.py" method="GET">
					<input type="hidden" name="'''+str(flights[1][0])+'''" value="get">
					<input type="hidden" name="date" value="'''+date+'''">
					<input type="submit" value="BOOK" class="book">
				</form>
				</div>
			</div>
			<div class="roundcorner1">
				<div class="airline-logo">
						<img src="https://s3-us-west-2.amazonaws.com/paytm-travel/travel_db/flights/airlines+logo/6E.png">
				</div>
				<div>
					<div class="airline-name">
						INDIGO
						<div class="airline-des">
							'''+str(flights[2][0])+''' 
						</div>
					</div>
				</div>
				<div class="airline-time">
					'''+str(flights[2][3])+'''  <img src="https://d274ft55l0imju.cloudfront.net/flights/icons/srp_arrow.svg">  '''+str(flights[1][4])+''' 
				</div>
				<div class="airline-price">
					<span>&#8377;</span>'''+str(flights[2][5])+''' 
				</div>
				<div>
				<form action="/cgi-bin/payments.py" method="GET">
					<input type="hidden" name="'''+str(flights[2][0])+'''" value="get">
					<input type="hidden" name="date" value="'''+date+'''">
					<input type="submit" value="BOOK" class="book">
				</form>
				</div>			</div>
			<div class="roundcorner1">
				<div class="airline-logo">
						<img src="https://s3-us-west-2.amazonaws.com/paytm-travel/travel_db/flights/airlines+logo/EY.png">
				</div>
				<div class="airline-name">
					AIR INDIA
					<div class="airline-des">
						'''+str(flights[3][0])+''' 
					</div>
				</div>
				<div class="airline-time">
					'''+str(flights[3][3])+''' <img src="https://d274ft55l0imju.cloudfront.net/flights/icons/srp_arrow.svg">  '''+str(flights[2][4])+''' 
				</div>
				<div class="airline-price">
					<span>&#8377;</span>'''+str(flights[3][5])+''' 
				</div>
				<div>
				<form action="/cgi-bin/payments.py" method="GET">
					<input type="hidden" name="'''+str(flights[3][0])+'''" value="get">
					<input type="hidden" name="date" value="'''+date+'''">
					<input type="submit" value="BOOK" class="book">
				</form>
				</div>
			</div>
		</div>
		<div class="back">
				<button class="book" onclick="op()">BACK</button>
			<div>
	</div>
</body>
</html>'''
print(page)
