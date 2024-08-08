import customtkinter as ctk
import os 
import json
from tkinter import ttk
import tkinter

# Window data
app = ctk.CTk()
app.geometry("400x600")
app.title("ConnectDrive")
app.resizable(False, False)

jsonreader = "Text didn't change"
filepath = "/CDIP.lock"
y_padding = 6

# Frames for EVERYTHING
frame_json = ctk.CTkFrame(master=app, width=300, height=100, bg="white")
frame_json.pack(padx=60, pady=20, fill="both", expand=False)

frame_jsonbutforip = ctk.CTkFrame(master=app, width=300, height=100, bg="white")
frame_jsonbutforip.pack(padx=60, pady=0, fill="both")

frame_other = ctk.CTkFrame(master=app, width=300, height=150, bg="white")
frame_other.pack(padx=60, pady=20, fill="both", expand=False)
# Bye bye frames! You will be missed :,)

# Start for reading the JSON file thing
label_jsonstuff = ctk.CTkLabel(master=frame_json, text="Status for JSON File")
label_jsonstuff.pack(pady=y_padding, padx=10)

label_jsonreader = ctk.CTkLabel(master=frame_json, text=jsonreader)
label_jsonreader.pack(pady=y_padding, padx=10)
# End for reading the thing for JSON

# Start of reporting IP
label_ip = ctk.CTkLabel(master=frame_jsonbutforip, text="IP of device", bg="white")
label_ip.pack(pady=y_padding, padx=10)

label_ip1 = ctk.CTkLabel(master=frame_jsonbutforip, text="-----", bg="white")
label_ip1.pack(pady=y_padding, padx=10)
# End of reporting IP

optionmenu = ctk.CTkOptionMenu(master=frame_jsonbutforip, values=["A:", "B:", "D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"])
optionmenu.pack(pady=y_padding, padx=10)


cb_autoconnect = ctk.CTkCheckBox(master=frame_other, text="Auto-Connect")
cb_autoconnect.pack(pady=y_padding, padx=10)

# Features of this program!
# Below me there is the GUI and other stuff
def DeviceFinder():
    # Letting you know when the code starts searching for an IP Address
    label_jsonreader.configure(text = "Searching 🔎")
    # dlvalue stands for Drive Letter value
    dlvalue = optionmenu.get()
    # This is for the DEV program only disables script to avoid 
    # the looping text in console
    # Printing the value to know that it works! DEV BUILD ONLY
    print(dlvalue)
    # This the selected DL value exists it will report it in the app
    if os.path.exists(dlvalue):
        label_jsonreader.configure(text = "Drive found but no JSON file!")
        # This joins the Drive letter and the /session.lock 
        fullpath = os.path.join(dlvalue, filepath)
        # Here is will search for the CDIP.lock file
        if os.path.exists(fullpath):
            label_jsonreader.configure(text = "JSON file Found!")
            with open(fullpath, "r") as f:
                data = json.load(f)
                for connect in data["connect"]:
                    print(connect["ip"])
                    print(connect["type"])
                    label_ip1.configure(text = connect['ip'])
                    auco = cb_autoconnect.get()
                    if auco == False:
                        label_jsonreader.configure(text = "Auto-Connect disabled | JSON file Found!")
                    if auco == True:
                        if connect["type"] == "mstsc":
                            app.withdraw()
                            app.destroy()
                            os.system('%s %s %s' % ("mstsc /v:", connect["ip"], "/prompt"))
                        elif connect["type"] == "ssh":
                            os.system('%s %s' % ("cmd | ssh", connect["ip"])) 
                            
        
    else:
        print('path does not exists')
        label_jsonreader.configure(text = "Drive not found :,(")
    app.after(1000, DeviceFinder)

def Info():
    tk = tkinter.Tk()
    tk.title("ConnectDrive - Other Stuff")
    tk.geometry("400x700")
    app.resizable(False, False)

    tkinter.Label(master=tk, text="Thank you for using ConnectDrive!").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="ConnectDrive is one of my bigger projects").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="which i came up with during class").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="Which by itself was inspired by").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="a video what Clabretro did about").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="the Sun Ray Thin Clients").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="I would not recommend using this program").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="to store server info that is publicly accessible").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="The file used by the program is in the Root of").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="the device named CDIP.lock").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="This program is open-source! cool right?").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="This program is still in Beta").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="so this program might change").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="i have alot of ideas for this").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="Version: 1.1 release - A MBD Project").pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="Boring info: Compile date: 9-August-2024 | Second public release").pack(pady=y_padding, padx=10)

def CreateFile():  
    tk = ctk.CTkToplevel()
    tk.title("ConnectDrive - Create file")
    tk.geometry("400x600")
    app.resizable(False, False)

    frame_deviceport = ctk.CTkFrame(master=tk, width=600, height=100, bg="white")
    frame_deviceport.pack(pady=5, padx=10, fill=None)

    frame_ip = ctk.CTkFrame(master=tk, width=600, height=100, bg="white")
    frame_ip.pack(pady=5, padx=10, fill=None)

    frame_ConMet = ctk.CTkFrame(master=tk, width=600, height=100, bg="white")
    frame_ConMet.pack(pady=5, padx=10, fill=None)

    frame_submit = ctk.CTkFrame(master=tk, width=600, height=100, bg="white")
    frame_submit.pack(pady=5, padx=10, fill=None)

    ctk.CTkLabel(master=frame_deviceport, text="Please select which port your device is plugged into?").pack(pady=y_padding, padx=10)
    ctk.CTkLabel(master=frame_deviceport, text="(REQUIRED)").pack(pady=y_padding, padx=10)
    optionmenu = ctk.CTkOptionMenu(master=frame_deviceport, values=["A:", "B:", "D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"])
    optionmenu.pack(pady=y_padding, padx=10)

    ctk.CTkLabel(master=frame_ip, text="What is the IP of the Device? example: 192.168.*.*").pack(pady=y_padding, padx=10)
    ctk.CTkLabel(master=frame_ip, text="(REQUIRED)").pack(pady=y_padding, padx=10)
    ipofdevice = ctk.CTkEntry(master=frame_ip)
    ipofdevice.pack(pady=y_padding, padx=10)

    ctk.CTkLabel(master=frame_ConMet, text="How would you like to connect?").pack(pady=y_padding, padx=10)
    ctk.CTkLabel(master=frame_ConMet, text="(REQUIRED)").pack(pady=y_padding, padx=10)
    ConMet = ctk.CTkOptionMenu(master=frame_ConMet, values=["mstsc", "ssh"])
    ConMet.pack(pady=y_padding, padx=10)

    ctk.CTkLabel(master=frame_submit, text="Create file").pack(pady=y_padding, padx=10)

    def Create():
        dlvalue1 = optionmenu.get()
        ipaddress = ipofdevice.get()
        connectionmethod = ConMet.get()
        jsondata = {
            "connect": [ 
                {
                    "ip": ipaddress, 
                    "type": connectionmethod,
                }
            ] 
        }
        print("Creating Connect file")
        pathtofile = os.path.join(dlvalue1, filepath)
        print(pathtofile)
        with open(pathtofile, "w") as f:
            json.dump(jsondata, f)

    ctk.CTkButton(master=frame_submit, text="Create file", command=Create).pack(pady=y_padding, padx=10)

def Connect():
    cb_autoconnect.select()
    cb_autoconnect.configure(state="disabled")

create = ctk.CTkButton(master=frame_other, text="Create File", command=CreateFile)
create.pack(pady=y_padding, padx=10)

settingsbutton = ctk.CTkButton(master=frame_other, text="Info", command=Info)
settingsbutton.pack(pady=y_padding, padx=10)

manconnect = ctk.CTkButton(master=frame_other, text="Connect", command=Connect)
manconnect.pack(pady=y_padding, padx=10)

DeviceFinder()
app.mainloop()
