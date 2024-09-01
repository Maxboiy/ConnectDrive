import customtkinter as ctk
import os 
import json
\import sys
# from pythonping import ping
import tkinter
from tkinter import messagebox

app = ctk.CTk()
app.geometry("400x600")
app.title("ConnectDrive")
app.resizable(False, False)

jsonreader = "Text didn't change"
filepath = "/CDIP.lock"
y_padding = 6
version_ = "v1.2 | Telnet support"
compile_date = "20-August-2024"
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
wnfile = "_files\Whatsnew.txt"
pathtown = os.path.join(base_path, wnfile)
infofile = "_files\info.txt"
pathtofo = os.path.join(base_path, infofile)

# Frames for EVERYTHING
frame_json = ctk.CTkFrame(master=app, width=300, height=100)
frame_json.pack(padx=60, pady=20, fill="both", expand=False)

frame_jsonbutforip = ctk.CTkFrame(master=app, width=300, height=100)
frame_jsonbutforip.pack(padx=60, pady=0, fill="both")

frame_other = ctk.CTkFrame(master=app, width=300, height=150)
frame_other.pack(padx=60, pady=20, fill="both", expand=False)
# Bye bye frames! You will be missed :,)

# Start for reading the JSON file thing
label_jsonstuff = ctk.CTkLabel(master=frame_json, text="Status for JSON File")
label_jsonstuff.pack(pady=y_padding, padx=10)

label_jsonreader = ctk.CTkLabel(master=frame_json, text=jsonreader)
label_jsonreader.pack(pady=y_padding, padx=10)
# End for reading the thing for JSON

# Start of Manual Connection
label_ip = ctk.CTkLabel(master=frame_jsonbutforip, text="Manual Connect")
label_ip.pack(pady=y_padding, padx=10)

check_ip = ctk.CTkCheckBox(master=frame_jsonbutforip, text="Connect manually")
check_ip.pack(pady=y_padding, padx=10)

input_ip = ctk.CTkEntry(master=frame_jsonbutforip, placeholder_text="IP")
input_ip.pack(pady=y_padding, padx=10)

mc_ct_pp = ctk.CTkOptionMenu(master=frame_jsonbutforip, values=["SSH", "Telnet", "mstsc"])
mc_ct_pp.pack(pady=y_padding, padx=10)

# End of Manual Connection
idkmbawr_ip = ctk.CTkLabel(master=frame_jsonbutforip, text="Drive letter")
idkmbawr_ip.pack(pady=y_padding, padx=10)

optionmenu = ctk.CTkOptionMenu(master=frame_jsonbutforip, values=["A:", "B:", "D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"])
optionmenu.pack(pady=y_padding, padx=10)


cb_autoconnect = ctk.CTkCheckBox(master=frame_other, text="Auto-Connect")
cb_autoconnect.pack(pady=y_padding, padx=10)

# Features of this program!
# Below me there is the GUI and other stuff
def DeviceFinder():
    mc_cch_ip = check_ip.get()
    if mc_cch_ip == True:
        label_jsonreader.configure(text = "MC Enabled! | Script is disabled!")
        print(mc_cch_ip)
        if mc_cch_ip == False:
            label_jsonreader.configure(text = "MC disabled! | Returning to normal process!")
    if mc_cch_ip == False:
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
                        input_ip.configure(placeholder_text=connect["ip"])
                        print(connect["ip"])
                        print(connect["type"])
                        auco = cb_autoconnect.get()
                        if auco == False:
                            label_jsonreader.configure(text = "Auto-Connect disabled | JSON file Found!")
                        if auco == True:
                            co_auco_true = messagebox.askyesno("Continue?", "Do you want to continue?")
                            if co_auco_true == True:
                                if connect["type"] == "mstsc":
                                    app.withdraw()
                                    app.destroy()
                                    os.system('%s %s %s' % ("mstsc /v:", connect["ip"], "/prompt"))
                                elif connect["type"] == "ssh":
                                    os.system('%s %s' % ("cmd | ssh", connect["ip"])) 
                                    app.withdraw()
                                    app.destroy()
                                    app.quit()
                                elif connect["type"] == "telnet":
                                    os.system('%s %s' % ("telnet", connect["ip"]))
                                    app.withdraw()
                                    app.destroy()
                                    app.quit()
                            elif co_auco_true == False:
                                print("User denied connection.") 
                                app.withdraw()
                                app.destroy()
                                app.quit()
                                
            
        else:
            print('path does not exists')
            label_jsonreader.configure(text = "Drive not found :,(")
        
    app.after(1000, DeviceFinder)

def Info():
    tk = tkinter.Tk()
    tk.title("CD - Info")
    tk.geometry("250x200")
    tk.resizable(False, False)

    def openinfo():
        os.startfile(pathtofo)

    def openwn():
        os.startfile(pathtown)

    tkinter.Button(master=tk, text="Info (TXT File)", command=openinfo).pack(pady=y_padding, padx=10)
    tkinter.Button(master=tk, text="Whats new? (TXT File)", command=openwn).pack(pady=y_padding, padx=10)
    tkinter.Label(master=tk, text="---------------------------------------------------------------------------------").pack(pady=1)
    tkinter.Label(master=tk, text="Boring info below").pack(pady=1)
    tkinter.Label(master=tk, text=version_).pack(pady=1, padx=10)
    tkinter.Label(master=tk, text="Compile date:").pack(pady=1, padx=10)
    tkinter.Label(master=tk, text=compile_date).pack(pady=1, padx=10)

def CreateFile():  
    tk = ctk.CTkToplevel()
    tk.title("ConnectDrive - Create file")
    tk.geometry("400x600")
    app.resizable(False, False)

    frame_deviceport = ctk.CTkFrame(master=tk, width=600, height=100)
    frame_deviceport.pack(pady=5, padx=10, fill=None)

    frame_ip = ctk.CTkFrame(master=tk, width=600, height=100)
    frame_ip.pack(pady=5, padx=10, fill=None)

    frame_ConMet = ctk.CTkFrame(master=tk, width=600, height=100)
    frame_ConMet.pack(pady=5, padx=10, fill=None)

    frame_submit = ctk.CTkFrame(master=tk, width=600, height=100)
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
    ConMet = ctk.CTkOptionMenu(master=frame_ConMet, values=["mstsc", "ssh", "telnet"])
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
        if os.path.exists(pathtofile):
            print("File exists! Waiting for consent to overwrite!")
            cr_confirm_overwrite = messagebox.askyesno("CD - Overwrite?", "Seems like this file already exists! Would you like to overwrite it?")
            if cr_confirm_overwrite == True:
                with open(pathtofile, "w") as f:
                    json.dump(jsondata, f)
                messagebox.showinfo("CD - File written!", "The file has been written!")
                tk.withdraw()
                tk.destroy()
                close
            elif cr_confirm_overwrite == False:
                messagebox.showinfo("CD - Overwrite cancelled!", "The CFW will now close! (file overwrite cancelled!)")
                tk.withdraw()
                tk.destroy()
                close
        with open(pathtofile, "w") as f:
            json.dump(jsondata, f)
        messagebox.showinfo("CD - File written!", "The file has been written!")
        tk.withdraw()
        tk.destroy()
        

    ctk.CTkButton(master=frame_submit, text="Create file", command=Create).pack(pady=y_padding, padx=10)

def Connect():
    cb_autoconnect.select()
    cb_autoconnect.configure(state="disabled")
    mc_connect = check_ip.get()
    if mc_connect == True:
        ip_mc = input_ip.get()
        ct_mc = mc_ct_pp.get()
        if ct_mc == "mstsc":
            app.withdraw()
            app.destroy()
            os.system('%s %s %s' % ("mstsc /v:", ip_mc, "/prompt"))
        elif ct_mc == "SSH":
            os.system('%s %s' % ("cmd | ssh", ip_mc)) 
            app.withdraw()
            app.destroy()
            app.quit()
        elif ct_mc == "Telnet":
            os.system('%s %s' % ("telnet", ip_mc))
            app.withdraw()
            app.destroy()
            app.quit()

create = ctk.CTkButton(master=frame_other, text="Create File", command=CreateFile)
create.pack(pady=y_padding, padx=10)

settingsbutton = ctk.CTkButton(master=frame_other, text="Info", command=Info)
settingsbutton.pack(pady=y_padding, padx=10)

manconnect = ctk.CTkButton(master=frame_other, text="Connect", command=Connect)
manconnect.pack(pady=y_padding, padx=10)

DeviceFinder()
app.mainloop()