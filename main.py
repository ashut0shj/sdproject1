import csv
import stdiomask
import os


def login(x):
    cc=[]
    file = open(x)
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)
    id=input("\nEnter your Acc number : \n").strip()
    password=stdiomask.getpass()
    if list([id,password]) in cc:
        return True
        #edit
    else:
        os.system('cls')
        print("!!!  INCORRECT CREDENTIALS  !!!\n          try again \n")
        login(x)

def new(x):

    cc=[]
    file = open(x)
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)
    
    cred=open(x,mode='a',newline='')
    writer=csv.writer(cred)
    id=input("Enter your Roll num : ").strip()
    s=1
    for i in cc:
        if id in i:
            s=0
            break
    if s==1:
        password=input("Enter your password : ")
        password2=input("Enter your password again : ")
        if password==password2:
            writer.writerow([id,password])
            print("!!! Account created successfully !!!") 
            os.system('cls')
            login(x)

    else:
        print("Account already exists !!!")
        new(x)
def screen2(x):
    c=int(input("1. LogIn\n2. New User\n"))
    if c==1:
        return login(x)
    elif c==2:
        new(x)

def mainscreen():
    stat=0
    os.system('cls')

    p="""                                                       IIIT Naya Raipur

                                                            WELCOME"""
    print(p)
    a="y"
    while a=="y":
        print("""  Enter your choice
                                        1 : Student
                                        2 : Management 
                                        
                                                                """)
        c=int(input("what is your choice : "))
        os.system('cls')
        if c==1:
            stat=screen2('studcred.csv')
        elif c==2:
            stat=screen2('mancred.csv')
        
        a=input('''\n\nDo you want to return back to home page ? (y/n)''').strip()

mainscreen()