#ATMOperation.py     <--------File Name and Module Name
from ATMExcept import DepositError, WithdrawError,InsuffFundError
bal=500.00  # Minimum amount in the account
def deposit():
    damt=float(input("Enter the deposit amount:"))   #valueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tYour Account XXXXXXXX123 Credited With INR: {}".format(damt))
        print("\tNow Your Account XXXXXXXX123 Balance After deposit:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter the withdrawal amount:"))   #ValueError
    if(wamt<=0):
        raise WithdrawError
    else:
        if(wamt+500>bal):
            raise InsuffFundError
        else:
            bal=bal-wamt
            print("\tYour Account XXXXXXXX123 Debited With INR: {}".format(wamt))
            print("\tNow Your Account XXXXXXXX123 Balance After withdrawal: {}".format(bal))
def balenq():
    print("\tYour Account XXXXXXXX123 Balance: {}".format(bal))