#!C:/Program Files (x86)/Python37-32/python.exe
import cgi, cgitb
cgitb.enable()
import cgi
import base64
import pandas as pd
import sqlite3,random
form = cgi.FieldStorage() 
# Get data from fields
print ("Content-type:text/html\r\n\r\n")
print('''<html>
<head>


<link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">
<style>
  
body {
  font-family: "Montserrat";
  line-height: 1;
  padding: 20px;
  height: 100%;
  background-image: url('https://pixelz.cc/wp-content/uploads/2017/01/vinyard-and-mountains-tuscany-italy-uhd-4k-wallpaper.jpg');
  background-size: cover;
  background-position: center;
  
}


.book{
    color: #fff;
    background-color: #F85E6A;
    font-weight: 400;
    height: 45px;
    font-size: 18px;
    border: none;
    width: 15%;
    border-radius: 4px;
    text-transform: uppercase;
    float: left;
    margin-left: 42%;
}
.book1{
    color: #fff;
    background-color: #F85E6A;
    font-weight: 400;
    height: 45px;
    font-size: 18px;
    border: none;
    width: 15%;
    border-radius: 4px;
    text-transform: uppercase;
    float: left;
    margin-left: 0%;
}

.demo-title {
  text-align: center;
  font-size: 3rem;
  margin-bottom: 50px;
}

.pricing-table {
  display: table;
  width: 700px;
}
.pricing-table .pricing-option {
  width: 100%;
  margin-left: 90px;
  background: white;
  float: left;
  padding: 2%;
  text-align: center;
  -webkit-transition: all .3s ease-in-out;
  transition: all .3s ease-in-out;
}
.pricing-table .pricing-option:nth-child(even) {
  margin: 0 2%;
}
.pricing-table .pricing-option:hover {
  cursor: pointer;
  box-shadow: 0px 2px 30px rgba(0, 0, 0, 0.3);
  -webkit-transform: scale(1.04);
          transform: scale(1.04);
}
.pricing-table .pricing-option:hover i, .pricing-table .pricing-option:hover h1, .pricing-table .pricing-option:hover span, .pricing-table .pricing-option:hover b {
  color: #F85E6A;
}
.pricing-table .pricing-option:hover .front {
  opacity: 0;
  visibility: hidden;
}
.pricing-table .pricing-option:hover .back {
  opacity: 1 !important;
  visibility: visible !important;
}
.pricing-table .pricing-option:hover .back a.button {
  -webkit-transform: translateY(0px) !important;
          transform: translateY(0px) !important;
}
.pricing-table .pricing-option hr {
  border: none;
  border-bottom: 1px solid #F0F0F0;
}
.pricing-table .pricing-option i {
  font-size: 3rem;
  color: #D8D8D8;
  -webkit-transition: all .3s ease-in-out;
  transition: all .3s ease-in-out;
}
.pricing-table .pricing-option h1 {
  margin: 10px 0;
  color: #212121;
  -webkit-transition: all .3s ease-in-out;
  transition: all .3s ease-in-out;
}
.pricing-table .pricing-option p {
  color: #999;
  padding: 0 10px;
  line-height: 1.3;
}
.pricing-table .pricing-option .price {
  position: relative;
}
.pricing-table .pricing-option .price .front span.price {
  font-size: 2rem;
  text-transform: uppercase;
  margin-top: 20px;
  display: block;
  font-weight: 700;
  position: relative;
}
.pricing-table .pricing-option .price .front span.price b {
  position: absolute;
  font-size: 1rem;
  margin-left: 2px;
  font-weight: 600;
}
.pricing-table .pricing-option .price .back {
  opacity: 0;
  visibility: hidden;
  -webkit-transition: all .3s ease-in-out;
  transition: all .3s ease-in-out;
}
.pricing-table .pricing-option .price .back a.button {
  background: #F85E6A;
  padding: 15px 20px;
  display: inline-block;
  text-decoration: none;
  color: white;
  position: absolute;
  font-size: 13px;
  top: -5px;
  left: 0;
  right: 0;
  width: 150px;
  margin: auto;
  text-transform: uppercase;
  -webkit-transform: translateY(20px);
          transform: translateY(20px);
  -webkit-transition: all .3s ease-in-out;
  transition: all .3s ease-in-out;
}
.pricing-table .pricing-option .price .back a.button:hover {
  background: #f62d3d;
}
.pricing-table{
    float: left;
    width: 1100px;
}
.pricing-option{
    float: left;
    width: 100%;
}

 screen and (max-width: 600px) {
  .pricing-table .pricing-option {
    padding: 5%;
    width: 90%;
  }
  .pricing-table .pricing-option:nth-child(even) {
    margin: 30px 0 !important;
  }
  .pricing-table{
      width: 700px;
  }
}
</style>
</head>
<body>''')

pid = form.getvalue('xyzz')
#print(pid)
print('''<form><input class= "book1"type=button value=<-BACK onclick=history.back(-1) style=color:black;/></form>''')
conn = sqlite3.connect('final.db')
cur = conn.execute('SELECT * FROM packages where PID=?',(pid,))
pid=[]
ffid=[]
city=[]
hid=[]
attr=[]
rid=[]
c=0
for i in cur:
    c=c+1
    pid.append(i[0])
    #print(pid)
    ffid.append(i[1])
    city.append(i[2])
    hid.append(i[3])
    attr.append(i[4])
    rid.append(i[5])
#print(pid)
attr=list(attr)
#print(ffid," ",city," ",hid," ",attr," ",rid," ")
addr=[ ]
name=[ ]
subcat=[]
count=0
#a=attr.split(",")
'''for j in a:
    print(j)
   # x=int(j)
    count=count+1
    cur_attr=conn.execute('select * from attraction where id=?',(attr[j],))
    for i in cur_attr:
        addr.append(i[0])
        name.append(i[6])
        subcat.append(i[7])'''
#print(addr," ",name," ",subcat," ")
#"Name:%s<br/>Address:attr_address:%s<br/>%s"


        
flight_src=[]
flight_dst=[]
flight_dep_time=[]
flight_arr_time=[]
flight_price=[]
for j in range(c):
    cur_ffid=conn.execute('select * from FLIGHTS where id=?',(ffid[j],))
    for i in cur_ffid:
        flight_src.append(i[1])
        flight_dst.append(i[2])
        flight_dep_time.append(i[3])
        flight_arr_time.append(i[4])
        flight_price.append(i[5])
#print(flight_src," ",flight_dst," ",flight_dep_time," ",flight_arr_time)



hotel_name=[]
hotel_addr=[]
hotel_stars=[]
hotel_cost=[]
for j in range(c):
    cur_hid=conn.execute('select * from accommodation where id=?',(hid[j],))

    for i in cur_hid:
        hotel_name.append(i[1])
        hotel_addr.append(i[3])
        hotel_stars.append(i[4])
        hotel_cost.append(i[5])

#print(hotel_name," ",hotel_addr," ",hotel_stars," ",hotel_cost)
        
restaurant_name=[]
restaurant_addr=[]
restaurant_stars=[]
restaurant_cost=[]
for j in range(c):
    cur_rid=conn.execute('select * from amsr where id=?',(rid[j],))
    count2=0
    for i in cur_rid:
        count2=count2+1
        restaurant_name.append(i[1])
        restaurant_addr.append(i[3])
        restaurant_stars.append(i[4])
        restaurant_cost.append(i[5])         
    


print("<h1 class=demo-title>%s</h1>" %city[0])

for i in range(c):
    print('''

<div class="pricing-table">
    <div class="pricing-option">''')
    print("<i class=>%s</i>" %city[0])
    print("<h1>Package:%s</h1>" %pid[i])
   
    print("<hr/>")
    print("<p>Restaurant: %s<br/>Address: %s<br/>Stars:%s<br/></p></p>" %(restaurant_name[i],restaurant_addr[i],restaurant_stars[i]))
    print("<p>Flight: %s<br/>Source:%s<br/>Destination: %s<br/>Departure time: %s<br/>Arrival time: %s<br/></p>" %(ffid[i],flight_src[i],flight_dst[i],flight_dep_time[i],flight_arr_time[i]))
    print("<p>Hotel Name: %s<br/>Address:%s<br/>Stars: %s<br/></p>" %(hotel_name[i],hotel_addr[i],hotel_stars[i]))
    print('''<form action="pkg_payment.py">Start date: <input type="date" name="Start"><br/><br/>''')
    uid_curr=conn.execute("select * from packages where pid=? and hid=?",(pid[i],hid[i]))
    for k in uid_curr:
        uid_pid=k[8]
        ccoost=k[6]
        #print(uid_pid)
    a=attr[i].split(",")
    #print("a="," ",a)
    count=0;
    for j in a:
        x=int(j)
       
        count=count+1
       
        cur_attr=conn.execute('select * from attraction where id=?',(x,))
        for i in cur_attr:
            addr.append(i[0])
            name.append(i[6])
            subcat.append(i[7])
    for j in range(count):
        print("<p>ATTRACTION: %s NAME: %s ADDRESS: %s </p><br/>" %(subcat[j],name[j],addr[j]))
    
    print('''<hr />
            <div class="price">
            <div class="front">''')
    print("<span class=price>%s<b>&#8377</b></span>" %ccoost)
    print('''       </div>
                   <div class="back">''')
    print('''</div></form>''' %uid_pid)
                        
    print('''  </div>
        </div>
    </div>
    ''')

      
  
print('''</body>
</html>
'''   )

