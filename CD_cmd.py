import sys
import json
import os
from pythonping import ping
import webbrowser

command = sys.argv[1]
auco_cmd = 0
ptcf = "/CDIP.lock"
dlv_warning_remind = 0
create_connect_method_cmd = "None selected"

if command == "-h":
    print("-----------ConnectDrive-----------")
    print("This is the command-line version of ConnectDrive")
    print("allowing you to skip the GUI and use it via the terminal!")
    print("------")
    print("-h               // Brings up this help menu")
    print("-d [driveletter] // Will run the connect script on the driveletter")
    print("-c               // auto-confirms (Intended with use -d)")
    print("-create          // This will let you create the CDIP.lock file from the terminal")
    print("-ts              // Help you troubleshoot if you can't connect to a server")
    print("-info            // Gives you information about this version of ConnectDrive")

elif command == "-d":
    dlv_cmd= sys.argv[2]
    print("-----------ConnectDrive-----------")
    print("Checking", dlv_cmd, "please wait...")
    try:
        command2 = sys.argv[3]
        if command2 == "-c":
            print("confirmed!")
            auco_cmd = 1
    except:
        print()
    if os.path.exists(dlv_cmd):
        print(dlv_cmd,"found!")
        print("Checking for CDIP.lock file...")
        cptf = os.path.join(dlv_cmd, ptcf)
        if os.path.exists(cptf):
            print("CDIP.lock file found!")
            with open(cptf, "r") as f:
                data = json.load(f)

            for connect in data["connect"]:
                if auco_cmd == 1:
                    print(connect["ip"])
                    print(connect["type"])
                    if connect["type"] == "mstsc":
                        os.system('%s %s %s' % ("mstsc /v:", connect["ip"], "/prompt"))
                    elif connect["type"] == "ssh":
                        os.system('%s %s' % ("ssh", connect["ip"]))
                elif auco_cmd == 0:
                    print("-----------ConnectDrive/confirm?-----------")
                    print("Would you like to connect to")
                    print(connect["ip"], "?")
                    print("Connecting method:")
                    print(connect["type"], )
                    print("-----------ConnectDrive/confirm?-----------")
                    print("Connect [Y/n]?")
                    connect_cmd = input("Select> ")
                    if connect_cmd == "Y":
                        print("Connecting...")
                        if connect["type"] == "mstsc":
                            os.system('%s %s %s' % ("mstsc /v:", connect["ip"], "/prompt"))
                        elif connect["type"] == "ssh":
                            os.system('%s %s' % ("ssh", connect["ip"]))
                    elif connect_cmd == "n":
                        print("Closing...")
                        close
        else: 
            print("Drive found! But no CDIP.lock file detected!", cptf)
            print("Check if the drive has the CDIP.lock file on it")
    else:
        print("Drive not found! Please check if the drive letter is correct!", dlv_cmd)

elif command == "-create":
    os.system("cls")
    print("-----------ConnectDrive/Create-----------")
    print("Welcome to the Create File Wizard! CFW")
    print("To continue we need the Drive letter for the drive your going to use")
    create_dlv_cmd = input("Drive letter >> ")
    if create_dlv_cmd == "C:":
        print("Sorry! But you can't write the file to your C: drive!")
    
    elif create_dlv_cmd == "c:":
        print("Sorry! But you can't write the file to your C: drive!")
    
    else:
        print("-----------ConnectDrive/Create-----------")
        print("Checking", create_dlv_cmd + "...")
        if os.path.exists(create_dlv_cmd):
            print(create_dlv_cmd, "exists! You can now continue!")
        else:
            print("-----------ConnectDrive/Create-----------")
            print("Seems like", create_dlv_cmd, "isn't plugged in! Would you like to continue?")
            print("If you continue we will warn you when you need to plug in the drive")
            print("Contine? [Y/n]")
            create_dlv_warning_cmd = input("Select >> ")
            if create_dlv_warning_cmd == "Y":
                print("Okay! We will remind you at the end!")
                dlv_warning_remind = 1
            elif create_dlv_warning_cmd == "n":
                close
        print("The CDIP.lock file will be on", create_dlv_cmd)
        print("-----------ConnectDrive/Create-----------")
        print("Which server do you want to connect to?")
        create_ip_cmd = input("IP address >> ")
        print("-----------ConnectDrive/Create-----------")
        print("Would you like to test the IP address to see if it works?")
        print("Will ping the IP provided [Y/n]")
        create_ping_cmd = input("Ping? >> ")
        if create_ping_cmd == "Y":
            print("Pinging", create_ip_cmd)
            ping(create_ip_cmd, verbose=True)
            print("If you keep getting Request timed out")
            print("Make sure the server your trying to connect to is")
            print("1 = Connected to the internet / same router as you")
            print("2 = Make sure it has Remote desktop / SSH turned on!")
            print("3 = The computer is turned on")
        elif create_ping_cmd == "n":
            print("Skipping ping...")
            
        print("-----------ConnectDrive/Create-----------")
        print("How would you like to connect to the IP address?")
        print("[1] = SSH (Via the terminal)")
        print("[2] = mstsc (Via screensharing)")
        create_connect_cmd = input("method >> ")
        print(dlv_warning_remind)
        if create_connect_cmd == "1":
            create_connect_method_cmd = "ssh"
        elif create_connect_cmd == "2":
            create_connect_method_cmd = "mstsc"
        if dlv_warning_remind == 1:
            while True:
                print("-----------ConnectDrive/Remind-----------")
                print("Please plug in your drive before we continue")
                input("Press enter to check")
                if os.path.exists(create_dlv_cmd):
                    break
                else:
                    print("Drive not found!")
        cptf = os.path.join(create_dlv_cmd, ptcf)
        os.system("cls")
        print("-----------ConnectDrive/Create-----------")
        print("Checking if CDIP.lock file already exists...")
        if os.path.exists(cptf):
            print("-----------ConnectDrive/File-already-exists-----------")
            print("WARNING: seems like the CDIP.lock file already exists!")
            print("Would you like to overwrite the current file?")
            print("[Yes/n]")
            create_overwrite_cmd = input("Overwrite? >> ")
            if create_overwrite_cmd == "Yes":
                print("Overwriten...")

            elif create_overwrite_cmd == "n":
                print("Write process cancelled by User!")
                close

            json_format = {
                "connect": [ 
                    {
                    "ip": create_ip_cmd, 
                    "type": create_connect_method_cmd,
                    }
                ] 
            }

            with open(cptf, "w") as f:
                json.dump(json_format, f)
            print("-----------ConnectDrive/Create-----------")
            print("Write complete!")
            print("IP =", create_ip_cmd)
            print("Connection method =", create_connect_method_cmd)
            print("-----------ConnectDrive/Create-----------")
            print("Would you like to connect?")
            print("[Y/n]")
            create_connect_pc_cmd = input("Connect? >> ")
            if create_connect_pc_cmd == "Y":
                with open(cptf, "r") as f:
                    data = json.load(f)

                for connect in data["connect"]:
                    print("Connecting...")
                    if connect["type"] == "mstsc":
                        os.system('%s %s %s' % ("mstsc /v:", connect["ip"], "/prompt"))
                    elif connect["type"] == "ssh":
                        os.system('%s %s' % ("ssh", connect["ip"]))
            elif create_connect_pc_cmd == "n":
                print("Goodbye!")
                close

elif command == "-ts":

    print("-----------ConnectDrive/Troubleshoot-----------")
    print("Welcome to the Troubleshooting page!")
    print("[1] = Ping the server")
    print("[2] = Look for file in drive")
    print("[3] = Exit")
    ts_menu_cmd = input("Select >> ")
    if ts_menu_cmd == "1":
        print("-----------ConnectDrive/Troubleshoot-----------")
        print("Ping your device or a custom URL / IP")
        print("[1] = IP address on Drive")
        print("[2] = Custom URL / IP")
        ts_ip_cmd = input("Select >> ")
        if ts_ip_cmd == "1":
            print("-----------ConnectDrive/Troubleshoot-----------")
            print("On which port is the drive?")
            ts_ip_dl_cmd = input("Port >> ")
            if os.path.exists(ts_ip_dl_cmd):
                print("Drive found! Checking connection file...")
                cptf = os.path.join(ts_ip_dl_cmd, ptcf)
                if os.path.exists(cptf):
                    print("File has been found! Pinging IP...")
                    print("-----------ConnectDrive/Troubleshoot-----------")
                    with open(cptf, "r") as f:
                        data = json.load(f)

                    for connect in data["connect"]:
                        ping(connect["ip"], verbose=True)
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        print("If you keep getting Request timed out")
                        print("Make sure the server your trying to connect to is")
                        print("1 = Connected to the internet / same router as you")
                        print("2 = Make sure it has Remote desktop / SSH turned on!")
                        print("3 = The computer is turned on")

        elif ts_ip_cmd == "2":
            print("-----------ConnectDrive/Troubleshoot-----------")
            print("Which URL / IP would you like to ping?")
            ts_ip_cu_cmd = input("IP / URL >> ") 
            ping(ts_ip_cu_cmd, verbose=True)
            print("-----------ConnectDrive/Troubleshoot-----------")
            print("If you keep getting Request timed out")
            print("Make sure the server your trying to connect to is")
            print("1 = Connected to the internet / same router as you")
            print("2 = Make sure it has Remote desktop / SSH turned on!")
            print("3 = The computer is turned on")       
                 
    elif ts_menu_cmd == "2":
        print("-----------ConnectDrive/Troubleshoot-----------")
        print("In which port is the drive?")
        ts_fich_cmd = input("Port >> ")
        if os.path.exists(ts_fich_cmd):
            print("-----------ConnectDrive/Troubleshoot-----------")
            print("Drive found! Checking for file...")
            cptf = os.path.join(ts_fich_cmd, ptcf)
            if os.path.exists(cptf):
                print("CDIP.lock has been found!")
                print("-----------ConnectDrive/Troubleshoot-----------")
                print("Check if the IP and the connection method is correct?")
                print("[Y/n]")
                ts_filecheck_cmd = input("Select >> ")
                if ts_filecheck_cmd == "Y":
                    print("-----------ConnectDrive/Troubleshoot-----------")
                    with open(cptf, "r") as f:
                        data = json.load(f)

                    for connect in data["connect"]:
                        print(connect["ip"])
                        print(connect["type"])
                    if connect["type"] == "mstsc" or "ssh":
                        print("The connections method is correct! Check if you IP works using the Ping tool")
                    else:
                        print("The connection method seems to be invalid! redo the setup or change it manually")

            else:
                print("The file hasn't been found! Please create one")
        else:
            print("We can't find the drive! Maybe check if the drive-letter is correct or if it's plugged in")


    
    elif ts_menu_cmd == "3":
        print()

elif command == "-info":
    print("Hello and Welcome to ConnectDrive but in the terminal!")
    print("ConnectDrive is one of my bigger projects, which im proud of!")
    print("")
    print("Whats new [1]")
    print("Open github [2]")
    print("Credits [3]")
    print("Exit [type anything expect 1, 2, 3 or 4 DO NOT USE 4 TO QUIT I WARNED YOU]")
    print("\n Version 1.1 | Compile date: 9-August-2024 | a MBD Project\n")
    info_menu_cmd = input("Select >> ")
    if info_menu_cmd == "1":
        print('''
-----------ConnectDrive-----------
Welcome to the Whats new page for ConnectDrive!
Learn whats new!

Current version: 1.1

Whats new?:
   + A way to interact with CD using the terminal
   + Changelog called 'Whats new'

Release dates:
   Release 0.1:  29-July-2024
   Release 1.0:  31-July-2024
   Release 1.1:  8-August-2024

What to expect in the future:
   This text format being better

Compiler:
   PyInstaller

A Project so huge i forget about it *Most of the times*

MBD Project // Made By Dico //
-----------ConnectDrive-----------
        ''')

    elif info_menu_cmd == "2":
        webbrowser.open("https://github.com/Maxboiy/ConnectDrive") 
    
    elif info_menu_cmd == "3":
        print("-----------ConnectDrive-----------")
        print("Credits:")
        print("   -Maxboiy   | Coding, Logo design and everything else\n")
        print("Inspiration:")
        print("   A video clabretro did on the Sun Ray Thin Clients\n")
        print("Compiler:")
        print("   PyInstaller\n")
        print("Special thanks to:")
        print("  -You        | for using this program")
    
    elif info_menu_cmd == "4":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("Got you")
        print("or i didn't, who knows")
