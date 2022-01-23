print("Welcome !\nPlease insert your Card")
print("Hi,Please do not Remove your Chip Card.\nLeave your Card Inserted during\nthe Entire Transaction")
language=int(input("Please Select Language"))
if language==1:
    print("English")
elif language==2:
    print("Hindi")
else:
    print("Punjabi")
account=34305537855
mypin=2484
total=455897
pin=int(input("Please Enter Your PIN"))
if pin==mypin:
    print("PIN GENERATION")
    transaction=int(input("Please Select Your Transaction\n1.Cash Withdrawal\n2.Balance Inquiry\n3.Deposit\n4.PIN Change"))
    if transaction==1:
        withdraw=float(input("Please Enter Amount to Withdrawal"))
        print("Cash Available:Rs.100,Rs.200,Rs.500,Rs.2000")
        if total>withdraw:
            balance=total-withdraw
            print("Your Transaction is Being Processed.\nPlease Wait")
            print("Please Collect Cash")
            print("Your Availbl Balance :",balance)
        else:
            print("Insufficient Balance")
    elif transaction==2:
        print("Your Balance is :",total)
    elif transaction==3:
        deposit=float(input("Enter Your Amount to Depost"))
        balance=total+deposit
        print("Success")
        print("Total Balance Now is :",balance)
    elif transaction==4:
        pinchange=int(input("you want to change your PIN code Yes/NO:"))
        if pinchange==1:
            print("Yes")
            ac=int(input("Please enter your account number:"))
            if ac==account:
                p=int(input("Please Enter Your Previous PINCode"))
                if p==mypin:
                    newpin=int(input("Please Enter Your New PIN Code :"))
                    print("Your New PIN Code is :",newpin)
                else:
                    print("Your PIN is Invalied")
            else:
                print("Your Account Number is Invalied")
        else:
            print("You Dont Want Change Your PIN Code")
    else:
        print("Choose Only Valied Transaction")
else:
    print("Your PIN is Invalied")