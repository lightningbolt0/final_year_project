from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import urllib
import json
from branca.element import Template, MacroElement
import urllib
import folium


                   
app = Flask(__name__)


html_page = """<!DOCTYPE HTML>
<html>
<head>
<title>Rough AJAX Test</title>
<script>
    function loadXMLDoc()
    {
        var req = new XMLHttpRequest()
        req.onreadystatechange = function()
        {
            if (req.readyState == 4)
            {
                if (req.status != 200)
                {
                    //error handling code here
                }
                else
                {
                    var response = JSON.parse(req.responseText)
                    var output ="<h1> OUTPUT DATA</h1>"+"<br>"
                    var dat ="<br>"
                    
                     for (key in response){
                          var value=response[key];
                          if(typeof value === 'response'){
                              console.log('{');
                              logRecursive(value)
                              console.log('}');
                          }else{
                                console.log(JSON.stringify(value, null, 2));



                        for (keyy in value){
                          var valuee=value[keyy];
                          if(typeof value === 'value'){
                              console.log('{');
                              logRecursive(valuee)
                              console.log('}');
                          }else{
                                console.log(JSON.stringify(valuee, null, 2));
                                output +=keyy+" : "+JSON.stringify(valuee, null, 2) + "<br>"


                                
                              
                               }
                                                       }
                            output+="<br><br>"

                              
                               }
                                                       }

                                                   
                     document.getElementById('myDiv').innerHTML = output

                }
            }
        }
    
        req.open('POST', '/searching')
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        var un = document.getElementById('scname').value
        var sec = document.getElementById('secret').value
        var postVars = 'username='+un+'&secret='+sec
        req.send(postVars)
        
        return false
    }
</script>
</head>
<body>
<h1>Search For an IP</h1>
<form action="" method="POST">
<input type="text" name="scname" id="scname">
<input type="hidden" name="secret" id="secret" value="shhh">
<input type="button" value="Submit" onclick="return loadXMLDoc()">
</form>
<div id="myDiv"></div>
</body>
</html>"""


@app.route('/search',methods = ['POST'])
def search_index():
    return html_page
        

@app.route('/searching', methods = ['POST'])
def ajax_request():
    out = request.form['username']

     #-----------------------FTP--------------------------------
    try:
        client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/FTP_DB?retryWrites=true&w=majority")
        db = client["FTP_DB"]
        ftp = db['ftp']
        a = ftp.find_one()
        a.pop("_id")
        aa = {"_ftp_":"the following is ftp data"}
        if out in a:
            aa.update(a[out])
        else:
            x={"ftp":"no FTP data on this IP"}
            aa.update(x)
    except:
        pass


    #-----------------------RDP--------------------------------
    try:
        client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/RDP_DB?retryWrites=true&w=majority")
        db = client["RDP_DB"]
        rdp = db['rdp']
        b = rdp.find_one()
        b.pop("_id")
        bb={"_rdp_":"the following data is rdp"}
        if out in b:
            bb.update(b[out])
        else:
            x={"rdp":"no RDP data on this IP"}
            bb.update(x)
    except:
        pass

    #-----------------------SMB--------------------------------
    try:
        client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/SMB_DB?retryWrites=true&w=majority")
        db = client["SMB_DB"]
        smb = db['smb']
        c = smb.find_one()
        c.pop("_id")
        cc={"_smb_":"the following data is smb"}
        if out in c:
            cc.update(c[out])
        else:
            x={"smb":"no SMB data on this IP"}
            cc.update(x)
    except:
        pass
    #-----------------------SMTP--------------------------------
    try:
        client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/SMTP_DB?retryWrites=true&w=majority")
        db = client["SMTP_DB"]
        smtp = db['smtp']
        d = smtp.find_one()
        d.pop("_id")
        dd={"_smtp_":"the following data is smtp"}
        if out in d:
            dd.update(d[out])
        else:
            x={"smb":"no SMB data on this IP"}
            dd.update(x)
    except:
        pass
    #-----------------------TELNET--------------------------------
    try:
        client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/TELNET_DB?retryWrites=true&w=majority")
        db = client["TELNET_DB"]
        telnet = db['telnet']
        e = telnet.find_one()
        e.pop("_id")
        ee={"_telnet_":"the following data is telnet"}
        if out in e:
            ee.update(e[out])
        else:
            x={"smb":"no TELNET data on this IP"}
            ee.update(x)
    except:
        pass
    z={"FTP":aa,"RDP":bb,"SMB":cc,"SMTP":dd,"TELNET":ee}


    #z=str(z)
    #return str(z)
    return jsonify(z)



#marker color{'blue', 'lightred', 'darkpurple', 'pink', 'lightgray', 'cadetblue', 'beige', 'lightgreen', 'lightblue', 'black', 'darkred', 'orange', 'darkgreen', 'purple', 'gray', 'red', 'green', 'white', 'darkblue'}.

@app.route('/map',methods = ['POST'])
def map_index():
    #folium_map = folium.Map((0,0), zoom_start=2)

    ftp_db_mark()
    rdp_db_mark()
    smb_db_mark()
    smtp_db_mark()
    telnet_db_mark()
    templates = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 200px;'>
     

<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:blue;opacity:0.7;'></span>FTP</li>
    <li><span style='background:green;opacity:0.7;'></span>RDP</li>
    <li><span style='background:#FF7F7F;opacity:0.7;'></span>SMB</li>
    <li><span style='background:red;opacity:0.7;'></span>SMTP</li>
    <li><span style='background:#e75480;opacity:0.7;'></span>Telnet</li>

  </ul>
</div>

 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

    macro = MacroElement()
    macro._template = Template(templates)
    folium_map.get_root().add_child(macro)
    
    
    return folium_map._repr_html_()



def ftp_db_mark():
    a_logged_in=[]
    a_connection_reset=[]
    a_lat=[]
    a_long=[]
    a_country=[]
    a_city=[]
    a_region=[]
    a_ip=[]
    client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/FTP_DB?retryWrites=true&w=majority")
    db = client["FTP_DB"]
    ftp = db['ftp']
    a = ftp.find_one()
    a.pop("_id")
    for key in a:
        x=a[key]
        a_ip.append(key)
        a_logged_in.append(x["logged_in"])
        a_connection_reset.append(x['connection_reset'])
        a_lat.append(x['latitude'])
        a_long.append(x['longitude'])
        a_region.append(x['region'])
        a_country.append(x['country'])
        a_city.append(x['city'])
    print(len(a_lat))
    for i in range(len(a_lat)):
        folium.Marker([str(a_lat[i]),str(a_long[i])],
                      popup="IP: "+str(a_ip[i])+" city:"+str(a_city[i])+" region:"+str(a_region[i])+" country:"+str(a_country[i])+" logged in:"+str(a_logged_in[i])+" connection reset:"+str(a_connection_reset[i])).add_to(folium_map)

def rdp_db_mark():
    b_scan_result=[]
    b_lat=[]
    b_long=[]
    b_country=[]
    b_city=[]
    b_region=[]
    b_ip=[]
    client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/RDP_DB?retryWrites=true&w=majority")
    db = client["RDP_DB"]
    rdp = db['rdp']
    b = rdp.find_one()
    b.pop("_id")
    for key in b:
        x=b[key]
        b_ip.append(key)
        b_scan_result.append(x["scan_result"])
        b_lat.append(x['latitude'])
        b_long.append(x['longitude'])
        b_region.append(x['region'])
        b_country.append(x['country'])
        b_city.append(x['city'])
    for i in range(len(b_lat)):
        folium.Marker([str(b_lat[i]),str(b_long[i])],popup="IP: "+str(b_ip[i])+" city:"+str(b_city[i])+" region:"+str(b_region[i])+" country:"+str(b_country[i])+" scan_result:"+str(b_scan_result[i]),
                          icon=folium.Icon(color="green")).add_to(folium_map)

def smb_db_mark():
    c_scan_result=[]
    c_lat=[]
    c_long=[]
    c_country=[]
    c_city=[]
    c_region=[]
    c_ip=[]
    client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/SMB_DB?retryWrites=true&w=majority")
    db = client["SMB_DB"]
    smb = db['smb']
    c = smb.find_one()
    c.pop("_id")
    for key in c:
        x=c[key]
        c_ip.append(key)
        c_scan_result.append(x["scan_result"])
        c_lat.append(x['latitude'])
        c_long.append(x['longitude'])
        c_region.append(x['region'])
        c_country.append(x['country'])
        c_city.append(x['city'])
    for i in range(len(c_lat)):
        folium.Marker([str(c_lat[i]),str(c_long[i])],popup="IP: "+str(c_ip[i])+" city:"+str(c_city[i])+" region:"+str(c_region[i])+" country:"+str(c_country[i])+" scan_result:"+str(c_scan_result[i]),
                          icon=folium.Icon(color="lightred")).add_to(folium_map)
        

def smtp_db_mark():
    d_logged_in=[]
    d_connection_reset=[]
    d_lat=[]
    d_long=[]
    d_country=[]
    d_city=[]
    d_region=[]
    d_ip=[]
    client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/SMTP_DB?retryWrites=true&w=majority")
    db = client["SMTP_DB"]
    smtp= db['smtp']
    d = smtp.find_one()
    d.pop("_id")
    for key in d:
        x=d[key]
        d_ip.append(key)
        d_logged_in.append(x["logged_in"])
        d_connection_reset.append(x['connection_reset'])
        d_lat.append(x['latitude'])
        d_long.append(x['longitude'])
        d_region.append(x['region'])
        d_country.append(x['country'])
        d_city.append(x['city'])
        
    for i in range(len(d_lat)):
        folium.Marker([str(d_lat[i]),str(d_long[i])],popup="IP: "+str(d_ip[i])+" city:"+str(d_city[i])+" region:"+str(d_region[i])+" country:"+str(d_country[i])+" logged_in:"+str(d_logged_in[i])+" connection_reset:"+str(d_connection_reset[i]),
                          icon=folium.Icon(color="red")).add_to(folium_map)
        

def telnet_db_mark():
    e_logged_in=[]
    e_connection_reset=[]
    e_lat=[]
    e_long=[]
    e_country=[]
    e_city=[]
    e_region=[]
    e_ip=[]
    client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/TELNET_DB?retryWrites=true&w=majority")
    db = client["TELNET_DB"]
    ftp = db['telnet']
    e = ftp.find_one()
    e.pop("_id")
    for key in e:
        x=e[key]
        e_ip.append(key)
        e_logged_in.append(x["logged_in"])
        e_connection_reset.append(x['connection_reset'])
        e_lat.append(x['latitude'])
        e_long.append(x['longitude'])
        e_region.append(x['region'])
        e_country.append(x['country'])
        e_city.append(x['city'])
    for i in range(len(e_lat)):
        folium.Marker([str(e_lat[i]),str(e_long[i])],
                      popup="IP: "+str(e_ip[i])+" city:"+str(e_city[i])+" region:"+str(e_region[i])+" country:"+str(e_country[i])+" logged in:"+str(e_logged_in[i])+" connection reset:"+str(e_connection_reset[i]),
                      icon=folium.Icon(color="pink")).add_to(folium_map)
        









@app.route('/')
def index():
    
    return render_template("index.html")


if __name__ == "__main__":
    folium_map = folium.Map((0,0), zoom_start=2)
    app.run(debug = True)
