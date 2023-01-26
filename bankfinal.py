# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 20:30:51 2023

@author: Skanda
"""
import time
l = ['Edwin','Roy']
#uw and uw1 are the roll no.s of employees
d = {1:1,2:2}
si = 0
si1 = 0
si2 = 0
userchoice = 0
d2 = {}
accbase = {}
accbase1 = {}
bankacc=12560
workingstatus1 = d.values()
print(workingstatus1)
    
    
    
print("Welcome to DSDC")
kl = int(input("Enter the no.of employees:"))
for j in range(kl):
    
    s = int(input("Enter a password to get to the job"))
    pas = 1345
    if(s==pas):
        print("Yes, you r in the job")
    elif(s!=pas):
        print("Enter the password correctly:")
   
print(workingstatus1)

        



m = int(input("Enter your rollNo. employee"))
if(m==1):
    print("Do you wanna accept the transaction?,Edwin")
    u = int(input("Enter the choice as 1 or 2 to accept or deny respectively,Edwin"))
    k = input("Enter the person name:")
    
    if(u==1):
            
            print("Iam Edwin")
            d2["Edwin"]="On duty"
            print(d2)
            
            print("ENter 4 for opening an account in our bank,Enter 5 for loans,Enter 6 for credit cards")
            mj = int(input("Enter a valid choice")) 
            if(mj==4):
                print("How much do you earn?")
                kl = int(input("Enter the amt."))
                if(kl>50000):
                    print("You are eligible for account creation"
                          )
            elif(mj==6):
                   print("We have a variety of credit cards available:")
                   print("1.Card1:Credit limit:8900,2.Premium:Credit limit:15600,3.Flex:Credit limit:21000,4.Royal:50000")
                   opp = int(input("Enter your choice for purchase"))
                   if(opp==1):
                       print("Your card has been purchased:")
                       
               
    elif(m==2 or u==2):
        print("do u wanna accept the transaction?,Roy")
        
        x = int(input("Enter the choice as 7 or 8 to accept or deny"))
        if(x==7):
           
            print("Iam Roy")
            d2["Roy"] = {"On Duty"}
            d2["Edwin"] = {"Not on Duty"}
            s = input("Enter your name")
            print("ENter 10 for opening an account in our bank")
            hk = int(input("Enter a valid choice"))
            if(hk==10):
                print("How much do you earn?")
                kg = int(input("Enter the amt."))
                if(kg>50000):
                    print("You are eligible for account creation"
                          )
                 
accbase[1]=k
print(accbase)
accbase[1]=s
print(accbase1)   

print("Congrats",k,"You have opened an account in our bank")
print("Give your choice as 3 for keeping up your deposit")

er = int(input("Enter your choice as 3 or 4 for making or not the deposit"))

if(er==3):
    km = int(input("Enter the amount"))
accbase[1]=(k,km)
print(accbase)    
print("Your initial deposit money has been credit to your account no.1 and give your coice 5 for further relationship with us")
hu = int(input("Enter your choice as 5 or 6"))
if(hu==5):
    print("ENter 4 for opening an account in our bank,Enter 55 for loans,Enter 6 for credit cards,enter 7 for bill payments,enter 8 for business supports")
    lk = int(input("Enter a choice"))
    if(lk==55):
        mm = int(input("Enter the principal amount of loan you are wanting for:"))
        print("Loan1:",mm,"@ interest of 0.6% for 3years")
        si+=mm*3*0.6/100
        
        print("Loan2:",mm,"@ interest of 2% for 5 years")
        si1+=mm*2*5/100
        print("Loan3",mm,"@ interest of 3.5% for 10 years")
        si2+=mm*3.5*10/100
        ux = int(input("Enter your choice as 100 or 101 or 102"))  
        if(ux==100):
            an = int(input("Enter your account number:"))
            if(an==1):
                print("Yess!!!,congrats,You hv purchased the loan")
                print("Also, you must pay the amount every year without fail")
                
                accbase[1]=(k,km+mm)
                bankacc-=mm
            
                print(accbase[1])
                print(bankacc)
                
                time.sleep(3.6)
                accbase[1]=(k,km-(si+mm))
                bankacc+=(mm+si)
                
            elif(an==2):
                print("Yess!!!,congrats,You hv purchased the loan")
                
                accbase[2]=(k,km+mm)
                bankacc-=mm
        
elif(hu==6):
    print("Thank you")
    nj = input("Enter your name,dear customer")
    print("Hey!,Welcome and thanks for choosing to bank with us,You will be connected to our team shortly")
    m = int(input("Enter your rollNo. employee"))
    if(m==1):
        print("Do you wanna accept the transaction?,Edwin")
        u = int(input("Enter the choice as 1 or 2 to accept or deny respectively,Edwin"))
        k = input("Enter the person name:")
        
        if(u==1):
                
                print("Iam Edwin")
                d2["Edwin"]="On duty"
                print(d2)
                
                print("ENter 4 for opening an account in our bank,Enter 5 for loans,Enter 6 for credit cards,enter 7 for bill payments,enter 8 for business supports")
                mj = int(input("Enter a valid choice")) 
                if(mj==4):
                    print("How much do you earn?")
                    kl = int(input("Enter the amt."))
                    if(kl>50000):
                        print("You are eligible for account creation"
                              )
                   
        elif(m==2 or u==2):
            print("do u wanna accept the transaction?,Roy")
            
            x = int(input("Enter the choice as 7 or 8 to accept or deny"))
            if(x==7):
               
                print("Iam Roy")
                d2["Roy"] = {"On Duty"}
                d2["Edwin"] = {"Not on Duty"}
                s = input("Enter your name")
                print("ENter 10 for opening an account in our bank")
                hk = int(input("Enter a valid choice"))
                if(hk==10):
                    print("How much do you earn?")
                    kg = int(input("Enter the amt."))
                    if(kg>50000):
                        print("You are eligible for account creation"
                              )
                    
                  
        
    


