from socket import *
import argparse
import threading

parser = argparse.ArgumentParser("Simple port scanner program") #Adds Argument Functionality to Program 
parser.add_argument("--ports", type=int, nargs="+", required=False, help="Scan the listed ports (1 2 3 ...). Scans 1-1024 by default")
parser.add_argument("--ip",  type=str,  required=False, help="Scan a target host. localhost by default." , )  
parser.add_argument("--input", type=str, required=False, help="Read a list of ports from a file")
parser.add_argument("--output", type=str, required=False, help="Write the results to a file")
args = parser.parse_args()

#Checks for arguments and sets variables to default values if not provided
if args.ports: 
    ports = args.ports
else: 
    ports = range(1, 1025)

if args.ip:
    serverName = args.ip
else:
    serverName = 'localhost'

if args.input:
    print("Reading from input file:", args.input)
    eof = False
    with open(args.input, "r") as f:
        for line in f:
            arr = line.split()
            serverName = arr[0]
            ports = range(int(arr[1]), int(arr[2]) + 1)

if args.output:
    print("Logging to output file:", args.output)
    output = True
else:
    output = False

#Known Port Services
port_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    194: "IRC",
    443: "SSL",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "Remote Desktop",
    5632: "PCAnywhere",
    5900: "VNC",
    25565: "Minecraft"
}

results = {} #Store results of scan for later
lock = threading.Lock() #Needed for threading to access resources properly

def scan(port, serverIP): #Scans a port on a server, stores results in dictionary 
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.settimeout(0.3)
        ret = clientSocket.connect_ex((serverIP, port))
        if ret == 0:
            with lock:
                str = f'Port {port}, is open'
            if(port in port_services): #Checks if in known services
                with lock:
                    str += f" - Service: {port_services[port]}"
            else:
                with lock:
                    str += " - Service: Unknown"
        else:
            with lock:
                str = f'Port {port}, is closed'
        results[port] = str
        clientSocket.close()
    except gaierror: #Error handling 
        print(gaierror)
        print('Host name could not be resolved')
        exit()
    except error:
        print(error)
        print('Could not connect to server')
        exit()


def main(): #Main function
    serverIP = gethostbyname(serverName) #Get IP of server in case domain name is given 
    print(f'Scanning {serverIP}')
    threads = []
    for port in ports:
        t = threading.Thread(target=scan, args=(port, serverName)) #Preps threading with scan function
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join() #Waits for all threads to finish before printing results
    for port in sorted(results): #If output is enabled, write to file. Otherwise, print to console
        if(output):
            with open(args.output, "a") as f:
                f.write(results[port] + "\n")
        else:
            print(results[port])
main()