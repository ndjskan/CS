ip = ...
port = ...

################


local = ("localhost", 9999)
login=True
import socket
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("conecting...")
con=False
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.connect(("2001:4860:4860::8888", 80))
ipv6 = str(s.getsockname()[0])
s.close()
try:
    cs.connect((str(ip) + ".tcp.eu.ngrok.io", port))
except:
    cs.connect(local)

try:
    cs.send(ipv6.encode("ascii"))
    sscm=cs.recv(32).decode("ascii")
    if sscm == "":
        print("apotuxia sundeshs")
    else:
        print(sscm)
    import socket

    while sscm != "":
        data=input("register{R} , login{L}: ")
        if data == "R" or data=="L" or data=="r" or data=="l":
            cs.send(data.encode("ascii"))
            break
    if data=="R" or data=="r":
        data2="0"
        while data2 != "2":
            data1 = input("username: ")
            cs.send(data1.encode("ascii"))
            data1 = input("password: ")
            cs.send(data1.encode("ascii"))
            data2 = cs.recv(1).decode("ascii")
            if data2 == "0":
                print("afto to onoma idi uparxei")
            if data2 == "1":
                print("to onoma kai o kodikos prepei na einai mikrotera apo 12 xarakthres")
            if data2 =="3":
                time=cs.recv(12).decode("ascii")
                cs.send("76".encode("ascii"))
                print("paracalo perimente",time,"deyterolepta")
                break

    if data=="L" or data=="l":
        data2="0"
        while data2 != "2":
            data1=input("username: ")
            cs.send(data1.encode("ascii"))
            data1 = input("password: ")
            cs.send(data1.encode("ascii"))
            data2 = cs.recv(24).decode("ascii")
            if data2 == "0":
                print("latos onoma h kodikos")
            if len(data2) > 3:
                inpt=input(": ")
                cs.send(inpt.encode("ascii"))
                inpt = input(": ")
                cs.send(inpt.encode("ascii"))
        cs.send("9".encode("ascii"))
        print("epituxhs sundesh!")
        print("\n"*2)

        while True:
            m = cs.recv(12).decode("ascii")
            if m != "404":
                print("xrhmata:", m, "€")
            print(" ")
            bet_amount = input("poso stoixhmatos: ")
            cs.send(bet_amount.encode("ascii"))
            print(" ")
            r_num = cs.recv(8).decode("ascii")
            cs.send("567".encode("ascii"))

            if r_num == "404":
                print("error")
            else:
                print("aritmos:", r_num)

except:
    print("apotuxia sundeshs")
