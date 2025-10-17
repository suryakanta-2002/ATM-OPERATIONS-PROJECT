#ATMMainproject.py   <--------------main project
from ATMExcept import DepositError,WithdrawError,InsuffFundError
from ATMMenu import menu
from ATMOperation import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDONT ENTER ZERO OR -VE VALUES FOR DEPOSIT")
                except ValueError:
                    print("\tDONT ENTER ALNUMS,STRS AND SYMBOLS FOR DEPOSIT")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("\tDONT ENTER ZERO OR -VE VALUES FOR WITHDRAW")
                except InsuffFundError:
                    print("\tYOUR ACCOUNT DOES NOT CONTAIN SUFFICIENT AMOUNT")
                except ValueError:
                    print("\tDONT ENTER ALNUMS,STRS AND SYMBOLS FOR WITHDRAW")
            case 3:
                balenq()
            case 4:
                print("\tTHANKS FOR USING THIS PROJECT")
                break
            case _:
                print("\tYour selection of operation is wrong try-again")
    except ValueError:
        print("\tDONT ENTER ALNUMS,STRS AND SYMBOLS FOR CHOICE TRY-AGAIN")