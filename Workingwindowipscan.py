import os 
import time 
import socket 
import subprocess 
ip = []
Memhostpartip = [] # Getting the host part ip 
Gateway_router = [] # Getting the gate way router name 
Dict_hostandip = {} # Getting the dictionary of the host ip and name  

def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip)
        print(str(host_ip)) 
        ip.append(str(host_ip)) # Getting the host ipv4 address 
        print("Host part ip "+str(host_ip).split(".")[2])
        Memhostpartip.append(str(host_ip).split(".")[2]) # Getting the host ip address of the system 
        if Memhostpartip != [] and ip != []:
            if len(Memhostpartip) and len(ip) >=2: 
               ip.remove(ip[0])  # remove the first ip scan data and getting the new one inside the list 
               Memhostpartip.remove(Memhostpartip[0]) #remove the host part ip from the list 
    except: 
        print("Unable to get Hostname and IP") 

get_Host_name_IP() # Running the scanning IPv4 scan 
print(Memhostpartip,ip)
# Scan all the host name and ip inside the network
 
for i in range(0,256): 
       os.system("nslookup 192.168."+str(Memhostpartip[0])+"."+str(i)) # Running loop ip address from the data of the local ip first scan         
       checkip_data = subprocess.check_output("nslookup 192.168."+str(Memhostpartip[0])+"."+str(i),shell=True) # Getting the ouput from the command to processing in the data host ip scan 
       print(checkip_data.decode().split(" ")) 
       gettingdata  = checkip_data.decode().split(" ") 
       if len(gettingdata) > 6:
           print("Detect the devices connected to the network","\a")
           print(gettingdata[0],gettingdata[2].split("\r\n"),gettingdata[4].split("\r\n"),gettingdata[8].split("\r\n"),gettingdata[10].split("\r\n")) # Getting the gateway router name        
           print("Host detected: ",gettingdata[8].split("\r\n")[0],gettingdata[10].split("\r\n")[0])
           Dict_hostandip[gettingdata[8].split("\r\n")[0]] = gettingdata[10].split("\r\n")[0]
           
       # Getting the time sleep to protect DNS time out 
       print(Dict_hostandip) # Getting the dictionary list of the host and and ip in the group 
       print("Number of host detected",len(Dict_hostandip)) 
       print("Host name list: ",Dict_hostandip.keys())
       for  ir in Dict_hostandip.keys(): 

              print("Hostname: ",ir,Dict_hostandip.get(ir))
