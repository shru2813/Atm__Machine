class Insufficient(Exception):
    pass
class Invalid(Exception):
    pass

class Bank_balance:
    def __init__(self,current_balance):
        self.current_balance = current_balance

    def deposite_amount(self, D_amount):

        try:
            if D_amount < 0:
                raise Invalid

            else:
                self.current_balance += D_amount
                print(f"Current balance {self.current_balance}")
        except Insufficient:
            print("Insufficient Balance")
        except Invalid:
            print("You have entered an invalid input")


    def withdraw_amount(self, W_amount):
        self.W_amount = W_amount

        try:
            if W_amount > self.current_balance:
                raise Insufficient
            if W_amount < 0:
                raise Invalid

            else:
                self.current_balance -= W_amount
                print(f"Current balance {self.current_balance}")
                print("Thank you")
        except Insufficient:
            print("Insufficient Balance")
        except Invalid:
            print("You have entered an invalid input")

bank = Bank_balance(1000)
flag = 1
while(flag):
    user_input = int(input("Enter 1 for deposite / Enter 2 for withdraw: "))
    if user_input == 2:
        amount = int(input("Enter the amount to withdraw: "))
        bank.withdraw_amount(amount)
    elif user_input == 1:
        amount = int(input("Deposite the amount: "))
        bank.deposite_amount(amount)

    flag = int(input("Do you want to continue enter :1 else enter :0 : "))
