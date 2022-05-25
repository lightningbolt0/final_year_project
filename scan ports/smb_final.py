import asyncio
from ip2geotools.databases.noncommercial import DbIpCity
import json
import os
import time
from pymongo import MongoClient
import urllib
from geopy.geocoders import Nominatim
import re

b="2M"
p=21
n=300
i=0

ip_data={}


async def scan(full_ip):
    proc = await asyncio.create_subprocess_exec(
     'zmap','-p','445',full_ip,'-o',str(full_ip),
     stdout=asyncio.subprocess.PIPE,
     stderr=asyncio.subprocess.PIPE)
    print ("_____ip : {0}  scan completed_____".format(full_ip))

async def scan2(full_ip):
    print("__scan "+full_ip+"__")
    if (os.path.isfile("{}".format(full_ip)) == True):
      if (os.stat(full_ip).st_size != 0):
        print("Port is open "+full_ip)
        try:
            geolocator = Nominatim(user_agent="app")
            country=""
            region=""
            city=""
            latitude=""
            longitude=""
            proc = await asyncio.create_subprocess_shell(
      'smbclient '+' -L '+full_ip+' -N',
     stdout=asyncio.subprocess.PIPE,
     stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await proc.communicate()
            if stdout:
                response = DbIpCity.get(full_ip, api_key='free')
                country=response.country
                region=response.region
                city=re.sub(r" ?\([^)]+\)", "", response.city)
                loc = geolocator.geocode(city).raw
                latitude=loc['lat']
                longitude=loc['lon']
                a={full_ip:{"scan_result":"data available","latitude":latitude,"longitude":longitude,"city":city,"region":region,"country":country}}
                ip_data.update(a)
            else:
                response = DbIpCity.get(full_ip, api_key='free')
                region=response.region
                country=response.country
                city=re.sub(r" ?\([^)]+\)", "", response.city)
                loc = geolocator.geocode(city).raw
                latitude=loc['lat']
                longitude=loc['lon']
                a={full_ip:{"scan_result":"data not available","latitude":latitude,"longitude":longitude,"city":city,"region":region,"country":country}}
                ip_data.update(a)
                
        except Exception as e:
            print(e)
        os.remove(str(full_ip))
      else:
        os.remove(str(full_ip))
        
def loop2(i1,i2,i3):
    i4=0
    try:
        while(i4<256 and i3<256 and i2<256):
                    full_ip=str(i1)+"."+str(i2)+"."+str(i3)+"."+str(i4)
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(scan2(full_ip))
                    i4=i4+1
    except Exception as e:
        print(e)

def start():
    ip1=213
    ip2=191
    ip3=222
    ip4=0
    try:
        while(ip1<256):
                    if(ip4<256 and ip3<256 and ip2<256):
                        full_ip=str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
                        "smbclient -L "+full_ip+" -N"
                        cmd="zmap "+"-B "+b+" -p "+str(p)+" "+full_ip
                        loop = asyncio.get_event_loop()
                        #await asyncio.wait_for(initial(cmd,full_ip),timeout=2)
                        loop.run_until_complete(scan(full_ip) )
                        #time.sleep(0.3)
                        #loop.run_until_complete(scan2(full_ip))
                        ip4=ip4+1
                    elif(ip4>255):
                        loop2(ip1,ip2,ip3)
                        ip4=0
                        ip3=ip3+1
                    elif(ip3>255):
                        ip3=0
                        ip2=ip2+1
                    elif(ip2>255):
                        ip2=0
                        ip1=ip1+1

    except Exception as e:
        print(e)





if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        client = MongoClient("mongodb+srv://randw:"+urllib.parse.quote("Cyber@Sec1995")+"@cluster0.uq5r7.mongodb.net/SMB_DB?retryWrites=true&w=majority")
        db = client["SMB_DB"]
        ftp = db['smb']
        ftp.insert_one(ip_data)
        """
        with open ('output.json','w') as f:
            json.dump(ip_data,f,indent=4)
            """
    
