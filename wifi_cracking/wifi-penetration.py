# this is my try at porting crach.sh to python
 #imports
import os
import time

#variables
what_mode = 99
main_path = os.getcwd()
file_name_list = {0: None}
#hashcat related
hashcat_file = None
wordlist = None
session_name = None
double_check = None
#word menue:
mentalist_or_crunch = None
crunch_options = None
#session menue
session_name_recoverie = "None"
#capture menue
capture_mode = None
#functions
def check_where_i_am():
    global what_mode
    if what_mode == 99:
        main_menue()
        check_where_i_am()
    if what_mode == 0:
        crack_in_hashcat()
        check_where_i_am()
    if what_mode == 1:
        wordlist_menue()
        check_where_i_am()
    if what_mode == 2:
        session_menue()
        check_where_i_am()
    if what_mode == 3:
        capture_mode()
        check_where_i_am()
    if what_mode == 4:
        dependencie_mode()
        check_where_i_am()
    if what_mode == 5:
        close()
    #0 to crack a file in hashcat
def crack_in_hashcat():
    global main_path
    global hashcat_file
    os.system('clear')
#get the cracking file
    print("select the file to crack")
    counter = 1
    for x in os.listdir(main_path + "/hashcat_files"):
        print(counter, ":", x, end=' ')
        file_name_list[counter] = x
        counter = counter + 1
    print()
    print("enter the Number corosponding to the file you want to crack")
    hashcat_file = file_name_list[int(input())]
    file_name_list.clear() #clear the to get the wordlist
#get the wordlist
    print("Select the Wordlist")
    counter = 1
    for x in os.listdir(main_path + "/wordlists"):
        print(counter, ":", x, end=" ")
        file_name_list[counter] = x
        counter = counter + 1
    print()
    print("enter the Number corosponding to the Wordlist you want to use")
    wordlist = file_name_list[int(input())]
    #ask for session name
    print("What should the session be called?")
    session_name = input("Enter the session name: ")
    #double check
    print("Please make shure that all information is correct")
    print("Hashcat file:" + hashcat_file)
    print("Wordlist:" + wordlist)
    print("Session Name:" + session_name)
    double_check = input("Enter yes to continue enter no to re enter all information: ")
    if double_check == "yes":
        os.system("hashcat -m 22000 -a 0 --session " + session_name + " " + "hashcat_files/" + hashcat_file + " " + "wordlists/" + wordlist)
    else:
        crack_in_hashcat()
    #main
def wordlist_menue():
    os.system("clear")
    global what_mode
    global mentalist_or_crunch
    global crunch_options
    mentalist_or_crunch = None
    print("What do you want to do?")
    print("Enter 1 to start mentalist")
    print("Enter 2 to start Crunch")
    mentalist_or_crunch = input("Enter 1 or 2: ")
    #print(mentalist_or_crunch)
    if mentalist_or_crunch == "1":
        os.system("./Mentalist")
    if mentalist_or_crunch == "2":
        print("please enter all options for crunch(use -o filename to save to file)")
        print("IMPORTANT!!! this is a unfinished feature it works but i will add my own proper crunch engine")
        crunch_options  = input("Enter all crunch options:")
        os.system("crunch " + crunch_options)
    what_mode = 99
def session_menue():
    global what_mode
    session_name_recoverie = input("Please enter the name of the session: ")
    os.system("hashcat --restore --session " + session_name_recoverie)
    time.sleep(5)
    what_mode = 99
def capture_mode():
    print("Enter 1 to open airgeddon")
    print ("Enter 2 to open wireshark")
    capture_mode = input("Enter 1 or 2: ")
    if int(capture_mode) == 1:
        os.system("sudo bash ./airgeddon/airgeddon.sh")
    elif int(capture_mode) == 2:
        os.system("sudo wireshark")
def dependencie_mode():
    print("work under construction")
def close():
    exit()

def main_menue():
    os.system('clear')
    print()
    print("What do you want to do?")
    print()
    print("Enter 0 to crack a file in hashcat")
    print("Enter 1 to get to the wordlist menue")
    print("Enter 2 to restore a session")
    print("enter 3 to enter the capture mode")
    print("enter 4 to open the dependencie installer")
    print("enter 5 to exit")
    print()
    global what_mode # defines that it shoud use the normal what_mode instead of a function specific one
    what_mode = int(input())
    check_where_i_am()
check_where_i_am()