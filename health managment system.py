
def add():
    print("press 1 for Harry 2 for Arslan 3 for Usman")
    v1=int(input("Enter a number between 1 to 3 : "))
    if v1==1:
        print("This is Harry portion")
        v2=int(input("Enter 1 for FOOD OF HARRY 2 for EXERCISE OF HARRY : "))
        if v2==1:
            v3=input("Enter food harry eat in day  :  ")
            with open("harryfood.txt","a") as op:
                op.write(str(getdate())+v3)
                print("\n")
                print("successfully wriiten")
        elif v2==2: 
            v3=input("enter exercise harry do in a day :  ")
            with open("harryexercise.txt","a") as op:
                op.write(str(getdate())," : "+v3)
                print("successfully written")  
    elif v1==2:
        print("This is Arslan portion")
        v2=int(input("Enter 1 for FOOD OF ARSLAN 2 for EXERCISE OF ARSLAN  :  "))
        if v2==1:
            v3=input("Enter food ARSLAN eat in day  :  ")
            with open("arslanfood.txt","a") as op:
                op.write(str(getdate())+v3)
                print("successfully written")
        elif v2==2:
            v3=input("enter exercise ARSLAN do in a day  :")
            with open("arslanexercise.txt","a") as op:
             op.write(str(getdate())+v3)
             print("successfully wriiten")
    elif v1==3:
        print("This is Usman portion")
        v2=int(input("Enter 1 for FOOD OF USMAN 2 for EXERCISE OF USMAN  :  "))
        if v2==1:
            v3=input("Enter food USMAN eat in day  :  ")
            with open("usmanfood.txt","a") as op:
                op.write(str(getdate())+v3)
                print("successfully written")
        elif v2==2:
            v3=input("enter exercise USMAN do in a day  :  ")
            with open("usmanexercise.txt","a") as op:
                op.write(str(getdate())+v3)
                print("successfully written")
def retreive():
 print("press 1 for Harry 2 for Arslan 3 for Usman ")
 v1=int(input("Enter a number between 1 to 3 :  "))
 if v1==1:
    print("This is Harry portion")
    v2=int(input("Enter 1 for FOOD OF HARRY 2 for EXERCISE OF HARRY  :  "))
    if v2==1:
        with open("harryfood.txt") as op:
            for i in op:
                print(i,end="\n")
    elif v2==2:
        with open("harryexercise.txt") as op:
            for i in op:
                print(i,end="\n")
 elif v1==2:
    print("This is ARSLAN portion")
    v2=int(input("Enter 1 for FOOD OF ARSLAN 2 for EXERCISE OF ARSLAN  :   "))
    if v2==1:
        with open("arslanfood.txt") as op:
            for i in op:
                print(i,end="\n")
    elif v2==2:
        with open("arslanexercise.txt") as op:
            for i in op:
                print(i,end="\n")
 elif v1==3:
    print("This is USMAN portion")
    v2=int(input("Enter 1 for FOOD OF USMAN 2 for EXERCISE OF USMAN :  "))
    if v2==1:
        with open("usmanfood.txt") as op:
            for i in op:
                print(i,end="\n")
    elif v2==2:
        with open("usmanexercise.txt") as op:
            for i in op:
                print(i,end="\n")
 print("--------PROGRAM END---------")
print("This is HEALTH MANAGMENT SYSTEM")
print("if data add press 1 if data retrive press 2")
a=int(input("chose the number  :   " ))
def getdate():
    import datetime
    return datetime.datetime.now()
if a==1:
    add()
elif a==2:
    retreive()