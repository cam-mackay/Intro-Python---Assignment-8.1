#Python Assignment 8.1
#Campbell Mackay


#parent class - BankAccount
class BankAccount:
    
    def __init__(self, num, bal):
        self.accountNumber = num
        self.balance = float(bal)
        print("A bank account has been created")
        print("The account number is " + str(self.accountNumber))
        print("The balance is $" + str(self.balance))
        
    def withdraw(self):
        userWithdraw = input("How much would you like to withdraw? ")
        self.balance = self.balance - float(userWithdraw)
        self.getBalance()
        
    def deposit(self):
        userDeposit = input("How much would you like to deposit? ")
        self.balance = self.balance + float(userDeposit)
        self.getBalance()

    def getBalance(self):
        print("Current account balance is: $" + str(self.balance))


#child class 1 - CheckingAccount
class CheckingAccount(BankAccount):
    
    def __init__(self, num, bal, fee, minBal):
        BankAccount.__init__(self, num, bal)
        self.accountFees = fee
        self.minimumBalance = minBal
        print("This account is a checking account")
        print("The account fee is $" + str(self.accountFees))
        print("The minimum balance is $" + str(self.minimumBalance))

    #not really sure how to implement this method into the program
    def deductFees(self):
        print("Deducting fee...")
        self.balance = self.balance - self.accountFees
        print("Balance after fee is now $" + str(self.balance))
        

    def checkMinimumBalance(self):
        print("Checking if account balance meets minimum balance...")
        print("")

        if float(self.balance) < self.minimumBalance:
            print("Account balance is too low")
            print("You must deposit $" + str(self.minimumBalance - self.balance) + " to meet the minimum account balance")
            self.deposit()
            self.checkMinimumBalance()
        else:
            print("Account balance meets minimum balance requirements")
        

#child class 2 - SavingsAccount
class SavingsAccount(BankAccount):

    def __init__(self, num, bal, intRate):
        BankAccount.__init__(self, num, bal)
        self.interestRate = intRate
        print("This account is a savings account")
        print("The interest rate is " + str(self.interestRate) + "%")

    #also unsure of how to implement this method into the program
    def addInterest(self):
        print("Adding " + str(self.interestRate) + "% interest to balance of $" + str(self.balance))
        self.balance = self.balance + (self.balance * self.interestRate/100)
        print("New balance after interest is $" + str(self.balance))
        

#main program
print("Welcome to the Banking Program")

try:
    flag1 = 0
    while flag1 == 0:
        print("")
        print("--Main Menu--")
        print("To open an account, press 1")
        print("To exit the program, press 2")
        loop1 = input("")

        if loop1 == '1':
            flag2 = 0
            while flag2 == 0:
                flag2 = 1
                print("")
                print("--Account Creation--")
                print("To open a Checking Account, press 1")
                print("To open a Savings Account, press 2")
                loop2 = input("")

                if loop2 == '1':
                    print("")
                    print("--Open a Checking Account--")
                    print("Minimum Balance is $50.00")
                    print("Monthly Account Fees are $5.00")
                    checkingAccountNumber = input("Enter an Account Number: ")
                    checkingAccountBalance = input("Enter Account Balance: $")
                    print("Please wait while account is created...")
                    print("")
                    my_checkingAccount = CheckingAccount(checkingAccountNumber, checkingAccountBalance, 5.0, 50.0)
                    my_checkingAccount.checkMinimumBalance()

                    flag3 = 0
                    while flag3 == 0:
                        print("")
                        print("--My Checking Account--")
                        print("What would you like to do?")
                        print("To make a deposit, press 1")
                        print("To make a withdrawal, press 2")
                        print("To check your balance, press 3")
                        print("To go to the Main Menu, press 4")
                        loop3 = input("")

                        if loop3 == '1':
                            my_checkingAccount.deposit()
                        elif loop3 == '2':
                            my_checkingAccount.withdraw()
                        elif loop3 == '3':
                            my_checkingAccount.getBalance()
                        elif loop3 == '4':
                            print("Exiting to Main Menu...")
                            flag3 = 1
                        else:
                            print("Command not recognized")
                    
                elif loop2 == '2':
                    print("")
                    print("--Open a Savings Account--")
                    print("Interest Rate is 2%")
                    savingsAccountNumber = input("Enter an Account Number: ")
                    savingsAccountBalance = input("Enter Account Balance: $")
                    print("Please wait while account is created...")
                    print("")
                    my_savingsAccount = SavingsAccount(savingsAccountNumber, savingsAccountBalance, 2)

                    flag4 = 0
                    while flag4 == 0:
                        print("")
                        print("--My Savings Account--")
                        print("What would you like to do?")
                        print("To make a deposit, press 1")
                        print("To make a withdrawal, press 2")
                        print("To check your balance, press 3")
                        print("To go to the Main Menu, press 4")
                        loop4 = input("")

                        if loop4 == '1':
                            my_savingsAccount.deposit()
                        elif loop4 == '2':
                            my_savingsAccount.withdraw()
                        elif loop4 == '3':
                            my_savingsAccount.getBalance()
                        elif loop4 == '4':
                            print("Exiting to Main Menu...")
                            flag4 = 1
                        else:
                            print("Command not recognized")

                    
                else:
                    print("Command not recognized")
                    flag2 = 0

        elif loop1 == '2':
            print("Exiting program...")
            flag1 = 1
        else:
            print("Command not recognized")
except:
    print("Great... you broke it.")
