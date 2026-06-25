'''pyhton program to calculate reamining balance after withdrawl'''

#taking inputs

current_balance = float(input("Enter current balance(in Rs:): "))
withdrawl_amount = float(input("enter withdrwal amount(in Rs):"))

#remaining balance

print("Remaining balance is(in Rs): ", current_balance- withdrawl_amount)
