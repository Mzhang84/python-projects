#ask for how much they will deposit
def deposit():
    #creates a loop till the user intputs a valid number
    while True:
        #assigning input to a variable
        amount = input("What would you like to deposit? $")
        #if the input is a number then execute
        if amount.isdigit():
            #converts string into integer
            amount = int(amount)
            #if the amount is bigger than 0 then break the loop
            if amount > 0:
                break
            #if number is 0 >= then print message and loop for input again
            else:
                print("Amount must be greater than 0")
        #if sting does not have numbers then print message and loop again
        else:
            print("Please enter a number")
    return amount

def main():
    balance = deposit()

main