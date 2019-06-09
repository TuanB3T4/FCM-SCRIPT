#!/usr/bin/python
#############################################
mess = """\033[33m  
                      ) _     _
                     ( (^)-~-(^)
___________________,-.\_( \033[91m6 6 \033[33m )__,-.___________________
|                  'M'   \   /   'M'                  |
|                         >o<                         |
|                \033[91mScript Deface Creator                \033[33m|
|                     \033[91mAuthor: B3T4                    \033[33m|
|   \033[91mGitHub: https://github.com/TuanB3T4/FCM-SCRIPT   \033[33m |
|_____________________________________________________|"""
print mess
print "\033[91m(Created by B3T4 ID)"
title = raw_input("\033[36mJudul title: ")
heading = raw_input("Font diatasi gambar: ")
imagelink = raw_input("Masukan link gambar jpg,png/gif (tengah): ")
bgimage = raw_input("Link gambar jpg/png (background): ")
message = raw_input("Pesan. gunakan kode <br> untuk text selanjutnya! : ")
textcolor = raw_input("Masukan warna font (contoh=green): ")
youtubeid = raw_input("Youtube kode (MUSIK): ")
aler = raw_input("Pesan pembuka: ")

#Open the index
fo = open("script.html","w")

messagescript1 = """<!DOCTYPE html><html>
<link rel="icon" type="image/gif" href="http://i62.tinypic.com/wanhu0.png">
<head>
<title>"""
messagescript2 = title

messagescript3 = """</title>
</head>
<body> 
<body bgcolor="#000000" background ="""

messagescript4 = bgimage

messagescript5 = """><div class='CenterDiv'>
<center>
<center><font face="pirata one" size="20">
<script>
farbbibliothek = new Array();
farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100");
farbbibliothek[1] = new Array("#00FF00","#000000","#00FF00","#00FF00");
farbbibliothek[2] = new Array("#00FF00","#FF0000","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00");
farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040");
farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000");
farbbibliothek[5] = new Array("#000000","#000000","#000000","#FFFFFF","#FFFFFF","#FFFFFF");
farbbibliothek[6] = new Array("#0000FF","#FFFF00");
farben = farbbibliothek[4];
function farbschrift()
{
for(var i=0 ; i<Buchstabe.length; i++)
{
document.all["a"+i].style.color=farben[i];
}
farbverlauf();
}
function string2array(text)
{
Buchstabe = new Array();
while(farben.length<text.length)
{
farben = farben.concat(farben);
}
k=0;
while(k<=text.length)
{
Buchstabe[k] = text.charAt(k);
k++;
}
}
function divserzeugen()
{
for(var i=0 ; i<Buchstabe.length; i++)
{
document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>");
}
farbschrift();
}
var a=1;
function farbverlauf()
{
for(var i=0 ; i<farben.length; i++)
{
farben[i-1]=farben[i];
}
farben[farben.length-1]=farben[-1];

setTimeout("farbschrift()",30);
}
// Zu Demonstrationszwecken*****************
var farbsatz=1;
function farbtauscher()
{
farben = farbbibliothek[farbsatz];
while(farben.length<text.length)
{
farben = farben.concat(farben);
}
farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001));
}
setInterval("farbtauscher()",5000);
text= "{=} Your Website Has Been Hacked {=}";

string2array(text);
divserzeugen();
//document.write(text);  
//
/*function expand() {
for(x = 0; x < 50; x++) {
window.moveTo(screen.availWidth * -(x - 50) / 100, screen.availHeight * -(x - 50) / 100);
window.resizeTo(screen.availWidth * x / 50, screen.availHeight * x / 50);
}
window.moveTo(0,0);
window.resizeTo(screen.availWidth, screen.availHeight);
}
expand();*/
</script>
</font> 
</center> 
	
<h1 class="t3x">	 
	<font color="white" style="text-shadow: 0 0 20px orange, 0 0 5px orange, 0 0 7px orange, 0 0 45px orange; font-weight:bold: orange;font-size:60px">[=] """

messagescript6 = heading

messagescript7 = """ [=]</font>
	</h1>
<img src=""" 

messagescript8 = imagelink

messagescript9 = """ width=840px height=420px>
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

<marquee behavior="scroll" direction="left" scrollamount="90" scrolldelay="40" width="100%">
<font color="green">___________________________________________________________</font></marquee>
<div style="text-shadow: 0px 0px 10px green;"><span style="color: white;"><font face="transformers"><b>Thanks To : <marquee scrollamount="5" direction="left" width="50%"><span style="color: red;"> <span style="color: red;">[ B3T4 ]<span style="color: red;"></b></marquee></font></div><script type="text/rocketscript">/*<![CDATA[*/new TypingText(document.getElementById("message"), 90, function(i){ var ar= new Array("_", " ", "_", " "); return "" +ar[i.length % ar.length]; });//Type out examples:TypingText.runAll();/*]]>*/</script>
<marquee behavior="scroll" direction="right" scrollamount="90" scrolldelay="40" width="100%">
<font color="green">___________________________________________________________</font></marquee>


<font face="Courier" color="green" size="6">Contact me</font> 
    <br>
 <font face="Courier" color="green" size="6">TuanB3T4@gmail.com</font>
 <br>	 
  
  <a href="https://api.whatsapp.com/send?phone=+6285694011450&text=*Assalamualaikum%20bang%20kok%20lu%20ganteng*"><font face="Courier" color="green" size="3">[+]Tuan B3T4[+]</a>  </br>
  
  
<br><br><br><br><br><br>

<font face="Courier" color="red" size="4">Copyright Tuan B3T4 2k19</font>  
</center>


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

messagescript17 = """<script>alert(""""

messagescript18 = aler

messagescript19 = """")</script>"""

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

print "\033[91mScript Berhasil Di buat!"
print "\033[91mTERIMAKASIH TELAH MENGGUNAKAN TOOLS INI"

fo.close()
