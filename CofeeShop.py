# coffeshop program 
from json.tool import main
print("---------------------------------------------------------------------------------------------")
print("                                    welcome to Cofee shop                                    ")#Title
print("---------------------------------------------------------------------------------------------")
print("Enter Your Name ")
name=input()#it takes name of costumer
print("\nThank you ----"+ name +"---- for giving us a chance to our service")#paste the name of costomer

print("\n\n-----------------------PRESS THE GIVEN NO OF YOUR ORDER----------------------------------")
def product():                                                  #function define of product list
    print(" 1: tea           10rs\n")
    print("2: lassi          25rs\n")
    print("3: ice creame     15rs\n")
    print("4: hot coffe      30rs\n")
    print("5: cold coffe     20rs\n")
    print("6: badam sheck    30rs\n")
product()
order=int(input())                                              #order taking
    
print("enter quantity??????")

qtt=int(input())
main
if qtt<=10:

    if order==1:
        print ("thank you , your TEA will  ready in 2 minutes ,please wait\n")
        a=10*qtt
        print("Done !!!! please pay given amount on counter")
        print(a)
    elif order==2:
        print("thank you , your LASSI will  ready in 2 minutes ,please wait\n")
        b=25*qtt
        print("Done !!!! please pay given amount on counter")
        print(b)
    elif order==3:
        print("thank you , your ICE CREAME will  ready in 2 minutes ,please wait\n")
        c=15*qtt
        print("Done !!!! please pay given amount on counter")
        print(c)
    elif order==4:
        print("thank you , your HOT COFFE will  ready in 2 minutes ,please wait\n")
        d=30*qtt
        print("Done !!!! please pay given amount on counter")
        print(d)
    elif order==5:
        print("thank you , your COLD COFFE will  ready in 2 minutes ,please wait\n")
        e=20*qtt
        print("Done !!!! please pay given amount on counter")
        print(e)
    elif order==6:
        print("thank you , your BADAM SHECK will  ready in 2 minutes ,please wait\n")
        f=30*qtt
        print("Done !!!! please pay given amount on counter")
        print(f)
    else :
        print("Sorry !!!!! please give appropriate order")
else :
    print("You cant get more than 10 coffes,at this time")
    exit
print("press enter to exit from program")
input()