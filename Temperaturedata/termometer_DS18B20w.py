#!/usr/bin/python
import datetime
import time
from time import gmtime, strftime
import http.client, urllib.request, urllib.parse, urllib.error
import time
#sleep = 5 # how many seconds to sleep between posts to the channel
key = 'VDXNURGJNEUA4YFZ'  # Thingspeak channel to update


#Report Raspberry Pi internal temperature to Thingspeak Channel
def thermometer(tempT):
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        casT = time.time();
        params = urllib.parse.urlencode({'field1': tempT, 'field2':casT, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(temp)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
            print("connection OK")
        except:
            print("connection failed")
        break
    

def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    #print('Device >' + id + '< has been found')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()
 
    return int(mytemp[1])
 
  except:
    return 99999
 
if __name__ == '__main__':
  # Script has been called directly
  #id = '28-03168bfbafff'
  #print ("Temp : " + '{:.3f}'.format(gettemp(id)/float(1000)))
  id = '28-051693e3fdff'
  print ("Temp : " + '{:.3f}'.format(gettemp(id)/float(1000)))
  
  print(time.time())
  #print(time.localtime())
  #id1 = '28-03168bfbafff'
  #name1 = 'DayData20180420' + id1 +'.txt'
  id2 = '28-051693e3fdff'
  name2 = 'DayData20180427_' + id2 +'.txt'
     
  #f = open('' + name1, 'a+')
  f2 = open('' + name2, 'a+')
  ii = 0
  print('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id2)/float(1000)))
  
  #cas = 60*60*24*6
  while (ii<500):
    i=0
    while (i<5): #ukladame data kazdou pul hodinu
      #print(i)  
      #f.write('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id1)/float(1000)))
      #print('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id1)/float(1000)))
      f2.write('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id2)/float(1000)))
      time.sleep(60)
      i = i + 1
    ii = ii + 1
    #f.close()
    f2.close()
    #f = open('' + name1, 'a+')
    f2 = open('' + name2, 'a+')
    print ("Ulozeni c. "+ str(ii))
    print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
    print('' + str(time.time()) +' {:.2f} \n'.format(gettemp(id2)/float(1000)))
    thermometer(gettemp(id2)/float(1000))
    #print(+' {:.3f} \n'.format(gettemp(id2)/float(1000)))
    print((gettemp(id2)/float(1000)))
    print('online ulozeni zanama')
         
  print ("Good bye!")
  #f.close()
  f2.close()
  
  