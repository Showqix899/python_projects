
def showBalance():
    print(F"Your Balance: ${amount:.2f}")
def getDeposite():
    balance=float(input("Enter Your Amount: "))
    if balance == 0:
        print("no amount is added to your account")
        return 0
    elif balance < 0:
        print("wrong amount")
        return 0
    else:
        return balance
def withdrawals():
    if amount < 100 and amount >= 0:
        print("Insufficeint Amount")
        return 0
    else:
        withdrawalsAmount=float(input("Enter Your Amount: "))
        print("Successfully Withdrawn")
        return withdrawalsAmount
    

amount=0
is_running=True

while is_running:
    print("Wellcome to Bank of Grindelwall:-")
    print("Your Choices:")
    print("1.Your Balance")
    print("2.Make a Deposite")
    print("3.Withdrawals")
    print("4.Exit")
    choice=int(input("Choose (1-4): "))
    if choice == 1:
        showBalance()
    elif choice ==2:
        amount+=getDeposite()
        print(f"Your Balance: ${amount:.2f}")
    elif choice == 3:
        amount-=withdrawals()
        print(f"Your Current Amount:${amount:.2f}")
    elif choice == 4:
        is_running=False