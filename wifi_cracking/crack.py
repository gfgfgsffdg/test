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
#functions
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
    print("Work under construction")
    #print("What do you want to do?")
    #print("Enter 1 to start mentalist")
    #print("Enter 2 to start Crunch")

def session_menue():
    print("work under construction")
def capture_mode():
    print("work under construction")
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
if what_mode == 99:
    main_menue()
if what_mode == 0:
    crack_in_hashcat()
if what_mode == 1:
    wordlist_menue()
if what_mode == 2:
    session_menue()
if what_mode == 3:
    capture_mode()
if what_mode == 4:
    dependencie_mode()
if what_mode == 5:
    close()