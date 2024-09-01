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
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
pr_files = "_files"
paths = os.path.join(base_path, pr_files)
wnfile = "Whatsnew.txt"
pathtown = os.path.join(paths, wnfile)
iffile = "info.txt"
pathtoif = os.path.join(paths, iffile)
compile_date = "20-August-2024"
version = "1.2 | Telnet support"

if command == "-h":
    print("-----------ConnectDrive-----------")
    print("This is the command-line version of ConnectDrive")
    print("allowing you to skip the GUI and use it via the terminal!\n")
    print("------Info------")
    print("-h               // Brings up this help menu")
    print("-info            // Gives you information about this version of ConnectDrive\n")
    print("------Connecting------")
    print("-c [driveletter]    // Will run the connect script on the driveletter")
    print("-confirm            // auto-confirms (Intended with use -d and -mc)")
    print("-mc [IP] [ms/sh/tn] // Connect to an IP address without creating a CDIP.lock file\n")
    print("------*hopefully* Making things work------")
    print("-create          // This will let you create the CDIP.lock file from the terminal")
    print("-ts              // Help you troubleshoot if you can't connect to a server")

elif command == "-c":
    dlv_cmd = sys.argv[2]
    print("-----------ConnectDrive-----------")
    print("Checking", dlv_cmd, "please wait...")
    try:
        command2 = sys.argv[3]
        if command2 == "-confirm":
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
                    elif connect["type"] == "telnet":
                        os.system('%s %s' % ("telnet", connect["ip"]))
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
                        elif connect["type"] == "telnet":
                            os.system('%s %s' % ("telnet", connect["ip"]))
                    elif connect_cmd == "n":
                        print("Closing...")
                        close
        else: 
            print("Drive found! But no CDIP.lock file detected!", cptf)
            print("Check if the drive has the CDIP.lock file on it")
    else:
        print("Drive not found! Please check if the drive letter is correct!", dlv_cmd)
elif command == "-mc":
    auco_mc = False
    ip_mc = "---"
    type_mc = "---"

    try:
        try_ip_mc = sys.argv[2]
        try_type_mc = sys.argv[3]
        try_con_mc = sys.argv[4]

        ip_mc = try_ip_mc
        type_mc = try_type_mc
        
        if try_con_mc == "-confirm":
            auco_mc = True
        
    except:
        print()
    
    try:
        try_ip_mc = sys.argv[2]
        try_type_mc = sys.argv[3]

        ip_mc = try_ip_mc
        type_mc = try_type_mc
    except:
        print()
    if auco_mc == False:
            print("-----------ConnectDrive-----------")
            print("You are currently connecting to")
            print("IP:", ip_mc)
            print("Using:", type_mc)
            print("-----------ConnectDrive-----------")
            print("Do you want to continue? [Y/n]")
            con_auco_mc = input("Contine? >> ")
            if con_auco_mc == "Y":
                auco_mc = True
            elif con_auco_mc == "n":
                print("Cancelled!")
                close
            else:
                print("Cancelled!")
                close

    if type_mc == "mstsc":
        os.system('%s %s' % ("mstsc /v:",ip_mc))
    elif type_mc == "ssh":
        os.system('%s %s' % ("ssh", ip_mc))
    elif type_mc == "telnet":
        os.system('%s %s' % ("telnet", ip_mc))
    else:
        try:
            try_ip_mc = sys.argv[2]

            nv_ip_mc = try_ip_mc
        except:
            print() # Triggers any time of the day
        print("Seems like you didn't enter a valid way too connect! Please enter one")
        nv_type_mc = input("[mstsc / ssh / telnet] >> ")
        if nv_type_mc == "mstsc":
            os.system('%s %s' % ("mstsc /v:",nv_ip_mc))
        elif nv_type_mc == "ssh":
            os.system('%s %s' % ("ssh", nv_ip_mc))
        elif nv_type_mc == "telnet":
            os.system('%s %s' % ("telnet", nv_ip_mc))
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
            print("-----------ConnectDrive/Create-----------")
            print("If you keep getting 'Request timed out'")
            print("Make sure the server / computer your trying to connect to is")
            print("1 = Connected to the internet / same router as you")
            print("2 = Make sure that the method your using to connect is turned on on both the client and the server")
            print("3 = The computer / server is turned on")
            print("4 = Your network / device allows pinging! Check your firewall settings")
        elif create_ping_cmd == "n":
            print("Skipping ping...")
            
        print("-----------ConnectDrive/Create-----------")
        print("How would you like to connect to the IP address?")
        print("-----------ConnectDrive/Terminal-----------")
        print("[1] = SSH")
        print("[2] = Telnet\n")
        print("-----------ConnectDrive/Screensharing-----------")
        print("[3] = mstsc (Remote Desktop Connection)\n")

        create_connect_cmd = input("method >> ")
        print(dlv_warning_remind)
        if create_connect_cmd == "1":
            create_connect_method_cmd = "ssh"
        elif create_connect_cmd == "3":
            create_connect_method_cmd = "mstsc"
        elif create_connect_cmd == "2":
            create_connect_method_cmd = "telnet"
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
            print("IP:", create_ip_cmd)
            print("Connection method:", create_connect_method_cmd)
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
                    elif connect["type"] == "telnet":
                        os.system('%s %s' % ("telnet", connect["ip"]))
            elif create_connect_pc_cmd == "n":
                print("Goodbye!")
                close
elif command == "-ts":

    print("-----------ConnectDrive/Troubleshoot-----------")
    print("Welcome to the Troubleshooting page!")
    print("[1] = Ping the server")
    print("[2] = Look for file in drive")
    print("[3] = Can't connect to a device using x")
    print("[4] = Exit")
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
                        print("-----------ConnectDrive/Create-----------")
                        print("If you keep getting 'Request timed out'")
                        print("Make sure the server / computer your trying to connect to is")
                        print("1 = Connected to the internet / same router as you")
                        print("2 = Make sure that the method your using to connect is turned on on both the client and the server")
                        print("3 = The computer / server is turned on")
                        print("4 = Your network / device allows pinging! Check your firewall settings")

        elif ts_ip_cmd == "2":
            print("-----------ConnectDrive/Troubleshoot-----------")
            print("Which URL / IP would you like to ping?")
            ts_ip_cu_cmd = input("IP / URL >> ") 
            ping(ts_ip_cu_cmd, verbose=True)
            print("-----------ConnectDrive/Create-----------")
            print("If you keep getting 'Request timed out'")
            print("Make sure the server / computer your trying to connect to is")
            print("1 = Connected to the internet / same router as you")
            print("2 = Make sure that the method your using to connect is turned on on both the client and the server")
            print("3 = The computer / server is turned on")
            print("4 = Your network / device allows pinging! Check your firewall settings")                      
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
                    if connect["type"] == "mstsc":
                        print("The connections method is correct! Check if you IP works using the Ping tool")
                    elif connect["type"] == "ssh":
                        print("The connections method is correct! Check if you IP works using the Ping tool")
                    elif connect["type"] == "telnet":
                        print("The connections method is correct! Check if you IP works using the Ping tool")
                    else:
                        print("The connection method seems to be invalid! redo the setup or change it manually")

            else:
                print("The file hasn't been found! Please create one")
        else:
            print("We can't find the drive! Maybe check if the drive-letter is correct or if it's plugged in")
    elif ts_menu_cmd == "3":
        os.system("cls")
        print("-----------ConnectDrive/Troubleshoot-----------")
        print("Please say what your using to connect")
        print("[1] = mstsc (Remote Desktop Connection)")
        print("[2] = ssh (Using the terminal)")
        print("[3] = telnet (Also using the terminal)\n")
        ts_cctdux_menu = input("Select >> ")
        if ts_cctdux_menu == "1":
            os.system("cls")
            print("-----------ConnectDrive/Troubleshoot-----------")
            print("Before we continue we are going to run a simple test")
            print("We're going to run the mstsc command which should open Remote Desktop Connection\n")
            print("Do you allow us to run 'mstsc'? [y/n]")
            cctdux_con_mstsc = input("Open? >> ")
            if cctdux_con_mstsc == "y":
                os.system("cls")
                print("-----------ConnectDrive/Troubleshoot-----------")
                print("The program has frozen because we openend Remote Desktop Connection! Please close it to continue")
                os.system("mstsc")
                os.system("cls")
                print("-----------ConnectDrive/Troubleshoot-----------")
                print("Did an another program open with the name Remote Desktop Connection? [y/n]\n") 
                cctdux_con_ordc = input("Did it? >> ")
                if cctdux_con_ordc == "y":
                    os.system("cls")
                    print("-----------ConnectDrive/Troubleshoot-----------")
                    print("Great! Now would you like us to run a example command?")
                    print("The command is 'mstsc /v:192.168.42.300' This should open Remote Desktop Connection and connect you to '192.168.42.300'")
                    print("Would you like to continue? [y/n]")
                    cctdux_con_rbc = input("Run? >> ")
                    if cctdux_con_rbc == "y":
                        os.system("cls")
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        print("The IP is not valid so it should time out")
                        print("Just click out of Remote Desktop Connection to continue")
                        os.system("mstsc /v:192.168.42.300")
                        os.system("cls")
                        print("Did an error pop-up?")
                        print("[y/n]\n")
                        cctdux_sts_done = input("Select >> ")
                        if cctdux_sts_done == "y":
                            print("-----------ConnectDrive/Troubleshoot-----------")
                            print("We're done! Seems like you didn't have any problems with mstsc!")
                            print("Now retry connecting if something went wrong the last time")
                            print("or to continue if you are testing to see if everything works\n")
                            print("Keep having problems?")
                            print("1. Check if you have entered the right drive letter\nBy opening the File explorer and checking which drive has the CDIP.lock file\n")
                            print("2. That the file isn't corrupted by going back into the troubleshoot menu and choosing 2\n")
                            print("3. Check if the IP of the device works by again going back to the troubleshoot menu and choosing 1\n")
                            print("4. If you keep getting errors please try a different version of ConnectDrive\nDon't worry! The file used by ConnectDrive works on all versions!\n")
                            print("5. If nothing else works we would recommend you create an issue on the official github")
                        elif cctdux_sts_done == "n":
                            print("-----------ConnectDrive/Troubleshoot-----------")
                            print("Try running the command yourself")
                            print("By typing in\n'mstsc /v:192.168.42.300'\n")
                            print("or using a custom IP")
                            print("If you get something like 'mstsc is not recognized'")
                            print("Please check that you have mstsc installed by opening the windows menu and typing 'mstsc'")
                            print("If you see something Remote Desktop Connection open it and check if it works\n")
                            print("if it does but the command doesn't we recommend just not using mstsc")
                    elif cctdux_con_rbc == "n":
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        print("We would recommend running the command yourself")
                        print("Run the command 'mstsc /v:192.168.42.300'")
                        print("If you keep getting an error like 'mstsc is not reconized'\nWe would recommend not using mstsc")
                elif cctdux_con_ordc == "n":
                    print("-----------ConnectDrive/Troubleshoot-----------")
                    print("Try running the command yourself\ntype or copy and paste the following 'mstsc' and press enter")
                    print("If you get an error that says 'mstsc is not reconized'\nThen we recommend not using mstsc")
            elif cctdux_con_mstsc == "n":
                print("-----------ConnectDrive/Troubleshoot-----------")
                print("Sorry we can't help you any further!")
        elif ts_cctdux_menu == "2":
            os.system("cls")
            print("-----------ConnectDrive/Troubleshoot-----------")
            print("First we need to see if we (as the program) can even use ssh")
            print("So we are going to run the command: 'ssh' Which should show you a list of commands\n")
            print("Do you allow us to run 'ssh'? [y/n]")
            cctdux_con_mstsc = input("Run? >> ")
            if cctdux_con_mstsc == "y":
                os.system("cls")        
                os.system("ssh")
                print("-----------ConnectDrive/Troubleshoot-----------")
                print("Do you see something like 'usage: ssh'? [y/n]\n") 
                cctdux_con_ordc = input("Did you? >> ")
                if cctdux_con_ordc == "y":
                    os.system("cls")
                    print("-----------ConnectDrive/Troubleshoot-----------")
                    print("Great! Now would you like us to run a example command?")
                    print("The command is 'ssh 192.168.42.300' This should connect you to '192.168.42.300' which is not a valid IP")
                    print("Would you like to continue? [y/n]")
                    cctdux_con_rbc = input("Run? >> ")
                    if cctdux_con_rbc == "y":
                        os.system("cls")
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        print("The IP is not valid and should time out")
                        print("Just wait a few secons to continue")
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        os.system("ssh 192.168.42.300")
                        print("Did you get an error message from ssh that said 'No such host is known.'?")
                        print("[y/n]\n")
                        cctdux_sts_done = input("Select >> ")
                        if cctdux_sts_done == "y":
                            os.system("cls")
                            print("-----------ConnectDrive/Troubleshoot-----------")
                            print("We're done! Seems like you didn't have any problems with ssh!")
                            print("Now retry connecting if something went wrong the last time")
                            print("or to continue if you are testing to see if everything works\n")
                            print("Keep having problems?")
                            print("1. Check if you have entered the right drive letter\nBy opening the File explorer and checking which drive has the CDIP.lock file\n")
                            print("2. That the file isn't corrupted by going back into the troubleshoot menu and choosing 2\n")
                            print("3. Check if the IP of the device works by again going back to the troubleshoot menu and choosing 1\n")
                            print("4. If you keep getting errors please try a different version of ConnectDrive\nDon't worry! The file used by ConnectDrive works on all versions!\n")
                            print("5. If nothing else works we would recommend you create an issue on the official github page")
                        elif cctdux_sts_done == "n":
                            print("-----------ConnectDrive/Troubleshoot-----------")
                            print("Try running the command yourself")
                            print("By typing in\n'ssh 192.168.42.300'\n")
                            print("If you get something like 'ssh is not recognized'")
                            print("Check if you have it installed by")
                            print("Opening settings > System > Optional Features > and check the list for OpenSSH Client\n")
                            print("If you can't see OpenSSH Client press 'Add a feature' on top of the page and searching for SSH Client not SSH server")
                    elif cctdux_con_rbc == "n":
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        print("Okay! Try running the command the command yourself by copy and pasting the command above")
                elif cctdux_con_ordc == "n":
                    print("-----------ConnectDrive/Troubleshoot-----------")
                    print("Try running the command yourself\ntype or copy and paste the following 'ssh' and press enter")
                    print("If you get an error that says 'ssh is not reconized'\nThen we recommend not using ssh")
            elif cctdux_con_mstsc == "n":
                print("-----------ConnectDrive/Troubleshoot-----------")
                print("Sorry we can't help you any further!")
        elif ts_cctdux_menu == "3":
            os.system("cls")
            print("-----------ConnectDrive/Troubleshoot-----------")
            print("First lets see if we can even use telnet")
            print("So we are going to run the command: 'telnet -h' Which should show you a list of commands\n")
            print("Do you allow us to run the command? [y/n]")
            cctdux_con_mstsc = input("Run? >> ")
            if cctdux_con_mstsc == "y":
                os.system("cls")        
                os.system("telnet -h")
                print("-----------ConnectDrive/Troubleshoot-----------")
                print("So do you see an list of commands? [y/n]\n") 
                cctdux_con_ordc = input("Do you? >> ")
                if cctdux_con_ordc == "y":
                    os.system("cls")
                    print("-----------ConnectDrive/Troubleshoot-----------")
                    print("Great! Now to follow up with the last command we will run a example command")
                    print("The command is 'telnet 192.168.42.300' This should try to connect to '192.168.42.300' which should not work as it is not an valid IP")
                    print("Would you like to continue? [y/n]")
                    cctdux_con_rbc = input("Run? >> ")
                    if cctdux_con_rbc == "y":
                        os.system("cls")
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        print("The IP we are connection to should time out or reject connection")
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        os.system("telnet 192.168.42.300")
                        print("Did you get an 'Connect Failed' error?")
                        print("[y/n]\n")
                        cctdux_sts_done = input("Select >> ")
                        if cctdux_sts_done == "y":
                            os.system("cls")
                            print("-----------ConnectDrive/Troubleshoot-----------")
                            print("We're done! Seems like you didn't have any problems with Telnet!")
                            print("Now retry connecting if something went wrong the last time")
                            print("or if you are testing to see if everything works well your done!\n")
                            print("Keep having problems?")
                            print("1. Check if you have entered the right drive letter\nBy opening the File explorer and checking which drive has the CDIP.lock file\n")
                            print("2. That the file isn't corrupted by going back into the troubleshoot menu and choosing 2\n")
                            print("3. Check if the IP of the device works by again going back to the troubleshoot menu and choosing 1\n")
                            print("4. If you keep getting errors please try a different version of ConnectDrive\nDon't worry! The file used by ConnectDrive works on all versions!\n")
                            print("5. If nothing else works we would recommend you create an issue on the official github page")
                        elif cctdux_sts_done == "n":
                            print("-----------ConnectDrive/Troubleshoot-----------")
                            print("Try running the command yourself")
                            print("By typing in\n'telnet 192.168.42.300'\n")
                            print("If you get something like 'telnet is not recognized'")
                            print("Check if you have it installed by")
                            print("Opening Control Panel > Programs > Programs and Features > on the left side panel click on\nTurn Windows features on or off")
                            print("Which should open a window with options, look for Telnet Client (A bit down the list) turn it on and press OK\nLet Windows search for files and after it's just restart the system and your done!")
                    elif cctdux_con_rbc == "n":
                        print("-----------ConnectDrive/Troubleshoot-----------")
                        print("Okay! Try running the command the command yourself by copy and pasting the command above")
                elif cctdux_con_ordc == "n":
                    print("-----------ConnectDrive/Troubleshoot-----------")
                    print("Try running the command yourself\ntype or copy and paste the following 'ssh' and press enter")
                    print("If you get an error that says 'ssh is not reconized'\nThen we recommend not using ssh")
            elif cctdux_con_mstsc == "n":
                print("-----------ConnectDrive/Troubleshoot-----------")
                print("Sorry we can't help you any further!")
    # This connection checker is 200 lines of code! Dang
    elif ts_menu_cmd == "4":
        print()
elif command == "-info":
    print("Hello and Welcome to ConnectDrive but in the terminal!")
    print("ConnectDrive is one of my bigger projects, which im proud of!")
    print("")
    print("Whats new [1]")
    print("Info [2]")
    print("Open github [3]")
    print("Credits [4]")
    print("Exit [type anything expect 1, 2, 3, 4 or 5]")
    print("\n Version ", version," | Compile date: ", compile_date," | a MBD Project\n")
    info_menu_cmd = input("Select >> ")
    if info_menu_cmd == "1":
        os.system('%s %s' % ('more', pathtown))

    elif info_menu_cmd == "2":
        os.system('%s %s' % ('more', pathtoif))

    elif info_menu_cmd == "3":
        webbrowser.open("https://github.com/Maxboiy/ConnectDrive") 
    
    elif info_menu_cmd == "4":
        print("-----------ConnectDrive-----------")
        print("Credits:")
        print("   -Maxboiy   | Coding, Logo design and everything else\n")
        print("Inspiration:")
        print("   -A video clabretro did on the Sun Ray Thin Clients\n")
        print("Compiler:")
        print("  -PyInstaller\n")
        print("Special thanks to:")
        print("  -You        | for using this program")

    elif info_menu_cmd == "5":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("Got you")
        print("or i didn't, who knows")
