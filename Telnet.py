import sys, socket, traceback, telnetlib as telnet
 
def openconn():
        temp=0
        while temp==0:
                try:
                        ip = str(input("What ip would you like to connect to?"))
                        port = input("And what port would you like to connect to?")
                       
 
                        global conn
                        conn=telnet.Telnet(ip,port,1)
                        print("Connected")
                        temp=1
                        break  
 
                except:
                        print("please ensure that you're entering a correct ip and port")
 
def communicate():
 
        temp = 0
        while temp==0:
                try:
                        sndmsg = input("Message:")
                        sndmsg = bytes(sndmsg, "ascii")
 
                        if sndmsg == b"close":
                                conn.close()
                                print("Connection closed")
                                temp=1
                                break
 
                        conn.write(sndmsg+b"\n")
                        print(conn.read_all())
 
                except BrokenPipeError:
                        print("Connection closed")
                        temp=1
 
                except:                        
                        print("Something went wrong.")
                        print(traceback.print_exc())
 
                        temp2 = 0
 
                        while temp2 ==0:
                                temp3 = input("Would you like to try again? (y/n)")
 
                                if temp3 is not 'y' and temp3 is not 'Y' and temp3 is not 'n' and temp3 is not 'N':
                                        print("You entered an incorrect key!")
 
                                if temp3 is 'y' or temp3 is 'Y':
                                        temp2=1
                       
                                if temp3 is 'n' or temp3 is 'N':
                                        temp = 1
                                        temp2 = 1
 
while True:
        openconn()
        communicate()
