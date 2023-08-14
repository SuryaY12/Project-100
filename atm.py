class atm:
    def __init__(self,cardnumber,pin):
        self.pin = pin
        self.cardnumber = cardnumber
    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl (self,cardbuner):
        print("25 dollars withdrawn")
card = atm(10,10)
print (card.withdrawl(10))