#ImportErrors
import pythonping 
import customtkinter
import paramiko
import re
#get passwords for ssh
list = open("password.txt", "r")
ip = list.readlines(1)
port = list.readlines(1)
username = list.readlines(2)
password = list.readlines(3)
#init custom tkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500")
root.title("Python app")
cpu_temperature = "test"
cpu_temp = customtkinter.CTkLabel(root, text=str(cpu_temperature), font=("arial", 100))
cpu_temp.pack()
gpu_temp = customtkinter.CTkLabel(root, text=str(cpu_temperature), font=("arial", 100))
#functions
def find_temp(resault1):
    global cpu_temp, root, gpu_temp
    pattern = r"CPU Temperature:\s+\+(\d+\.\d+)°C"
    match = re.search(pattern, resault1)
#    pattern1 = r"edge: +.*[0-9]*\.[0-9]+°C"
#    match2 = re.search(pattern1, resault1)
    # If a match is found, extract the cpu_temperature
    if match:
        cpu_temperature = match.group(1)
        #gpu_temperatur = match2.group(0)
        cpu_temp.configure(text=str(cpu_temperature))

#variables
response = None
is_up = False
ssh = paramiko.SSHClient()  # Instantiate SSHClient object
#main
def get_data():
#check if host is up
    global root, cpu_temp, gpu_temp
    response = pythonping.ping(str(ip)[2:17], verbose= True)
    for response1 in response:
        if response1.success:
            is_up = True
        else:
            is_up = False
        if is_up == True:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=str(ip)[2:17], port=int(22), username=str(username)[2:5], password=str(password)[2:25])
            stdin, stdout, stderr = ssh.exec_command("sensors")
                # Read the standard output from the command
            output = stdout.read().decode('utf-8')
            ssh.close()

            find_temp(str(output))
    root.after(10, get_data)
get_data()

root.mainloop()