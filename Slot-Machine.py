import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


#how much the symbols will appear, Ds will appear a lot
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4, 
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winning_lines = []
    winnings = 0
    #for every line you chose
    for line in range(lines):
        #records the leftmost item
        symbol = columns[0][line]
        #for each column
        for column in columns:
            symbol_to_check = column[line]
            #if symbol is not the same then don't give winnings
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            # +1 to get the right line # instead of index
            winning_lines.append(line + 1)
    return winnings, winning_lines
    

#rows, cols, symbols are in the parameters so that the function can use them
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #for every item in the dictionary
    #.items will give you the key and the value to the dictionary, it'll grab all the things in there
    #symbol is the key so "A"
    #symbol_count is the value so "2" 
    for symbol, symbol_count in symbols.items():
        #for variable in the range which is the value ex. "2"
        #underscore is an anonymus variable
        for _ in range(symbol_count):
            #adds "A" 2 times to the list
            all_symbols.append(symbol)
    #values in the columns      
    columns = []
    #for execute function every columns
    for _ in range(cols):
        column = []
        #[:] splice makes a copy of all_symbols
        current_symbols = all_symbols[:]
        #for every row in rows
        for _ in range(rows):
            #assign value to a random symbol from the all_symbols list
            value = random.choice(all_symbols)
            #removes value from the list of current symbols
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#will print out the numbers vertically
def print_slot_machine(columns):
    #for every row that the first column has
    for row in range(len(columns[0])):
        #for every items in the columns 
        #enumerates grabs the index
        for i, column in enumerate(columns):
            #if index is not the last index then print this
            #done to add bars to the ends of the first and second columns
            """last column has the biggest index so -1 will 
            give us the index version of the column"""
            if i != len(columns) -1:
                #ends the print with " | "
                print(column[row], end =" | ")
            #if i does equal the last index then print this
            else:
                print(column[row], end = "")
        #creates a new line for the next row to print
        print()

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

#similar to deposit, ask for lines and checks if its a valid number
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else: 
            print("Please enter a number.")
    return lines

#similar to deposit, checks if number is valid and in between MIN_BET and MAX_BET
def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else: 
            print("Please enter a number.")
    return amount

def spin(balance): 
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"YOu do not have enough to bet that amount, your balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

#main function that'll execute all the other functions
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if spin == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
    

main()