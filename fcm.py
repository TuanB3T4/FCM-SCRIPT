#!/usr/bin/python
#######################
#  http://fb.com/B3T4.id.9  #
#######################
mess = """
"\033[33m                     ) _     _
                     ( (^)-~-(^)
___________________,-.\_( 6 6 )__,-.___________________
|                  'M'   \   /   'M'                  |
|                         >o<                         |
|                Deface Script Creator                |
|                       B3T4 ID.                      |
|_____________________________________________________|"""
print mess
print "Created by B3T4 ID"
title = raw_input("Judul title: ")
heading = raw_input("Hacked by: ")
imagelink = raw_input("link gambar (tengah): ")
bgimage = raw_input("link gambar (background): ")
message = raw_input("Pesan. gunakan kode <br> untuk text selanjutnya! : ")
textcolor = raw_input("Warna text (contoh=green): ")
youtubeid = raw_input("youtube kode (MUSIK): ")


#Open the index
fo = open("script.html","w")

messagescript1 = """<html><head><title>"""

messagescript2 = title

messagescript3 = """</title></head>
<body>
<br>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Anton' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Josefin Sans' rel='stylesheet' type='text/css'>
<body bgcolor="#000000" background ="""

messagescript4 = bgimage

messagescript5 = """>	<h1 class="t3x">	 
	<font color="white" style="text-shadow: 0 0 20px orange, 0 0 5px orange, 0 0 7px orange, 0 0 45px orange; font-weight:bold: orange;font-size:60px">"""
messagescript6 = heading

messagescript7 = """</font>
	<font color="black" style="color:black;text-shadow: 0 0 3px red, 0px 0px 5px red;font-size:60;"></font>
	<font color="white" style="text-shadow: 0 0 20px black, 0 0 5px black, 0 0 7px black, 0 0 45px black; font-weight:bold: blue;font-size:60px"></font>
	</h1>
<img src=""" 

messagescript8 = imagelink

messagescript9 = """ width=450px height=340px>
<body onload="init()"></body>
<body>
<div id="bulle"></div>"""

messagescript10 = """
<script language=\"JavaScript\">
var i=0
var j=0
var texteNE, affiche
var texte=\"<br><br><br><br><br><font face=Orbitron color="""

messagescript11 = textcolor

messagescript12 = """ size=4>"""

messagescript13 = message 

messagescript14 = """<br><br></font><br></b></div>\"
var ie = (document.all);
var ne = (document.layers); 
function init(){
texteNE='';
machine_a_ecrire();
}
function machine_a_ecrire(){
texteNE=texteNE+texte.charAt(i)
affiche='<font face=Orbitron size=1 color=#ffffff><strong>Messenge : '+texteNE+'</strong></font>'
if (texte.charAt(i)=="<") {
j=1
}
if (texte.charAt(i)==">") {
j=0
}
if (j==0) {
if (document.getElementById) { // avec internet explorer
document.getElementById("bulle").innerHTML = affiche;
}
}
if (i<texte.length-1){
i++
setTimeout("machine_a_ecrire()",70)
}
else
return
}
</script><font face="Orbitron" size="1"><blink><span style="color: rgb(255, 255, 255);"><b><font color=lime size=4></font></b></u></blink><br></font></b>
<a href="/index.php"><img style="position:fixed;bottom:0px;z-index:1000;right:-10px;"  src="http://static1.squarespace.com/static/5706c12007eaa0b82399660d/5706c68bf0bc33987cae6c71/577d5c5d37c581fd0e25c10b/1469717705608/insult-145142_1280.png" type="image/gif" width="150"></a></body>
<!-- CSS --><style>
.t3x { font-family: pirata one; -webkit-animation-name: blinker; -webkit-animation-duration: 2s; -webkit-animation-timing-function: linear; -webkit-animation-iteration-count: infinite; -moz-animation-name: blinker; -moz-animation-duration: 1s; -moz-animation-timing-function: linear; -moz-animation-iteration-count: infinite; animation-name: blinker; animation-duration: 1s; animation-timing-function: linear; animation-iteration-count: infinite; color: #385164; } @-moz-keyframes blinker { 0% { opacity: 1.0; } 50% { opacity: 0.0; } 100% { opacity: 1.0; } } @-webkit-keyframes blinker { 0% { opacity: 1.0; } 50% { opacity: 0.0; } 100% { opacity: 1.0; } } @keyframes blinker { 0% { opacity: 1.0; } 50% { opacity: 0.0; } 100% { opacity: 1.0; } } } 
.CenterDiv{width:650px;border:1px #ff0000 solid;padding:5px;margin:0px auto; background: url('http://i.imgur.com/sDbaMsW.gif');}
</style>
<br>
<br>
<br>
<iframe width="0" height="0" src="http://www.youtube.com/v/"""

messagescript15 = youtubeid

messagescript16 = """&autoplay=1" frameborder="0"></iframe>"""


fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)

print "Script Berhasil Di buat!"
print "Kontak : fb.com/B3T4.id.9"

fo.close()
