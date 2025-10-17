#ATMExcept.py  <--------File Name and Module Name
class DepositError(Exception):pass
class WithdrawError(BaseException):pass
class InsuffFundError(Exception):pass