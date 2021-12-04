    
class AtmCard:
    #constructor
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def check_balance(self):
        print("Your Balance is 500000")

    def withdraw(self,amount):
        newAmount=500000-amount
        print("you have withdrawn amount "+str(amount)+" Remaining balance is:"+str(newAmount))


def main():
    cardNumber=input("insert your card number:")
    Pin=input("insert your  pin:") 

    #creating object of the class
    user= AtmCard(cardNumber,Pin) 

    print("select your action")
    print("1.Check Balance,2.Withdrawl")
    action=int(input("action number:"))

    if(action==1):
        user.check_balance()
    elif(action==2):
        amount=int(input("enter the amount:"))
        user.withdraw(amount)
    else:
        print("invalid choices")  

if __name__=="__main__":
    main()          