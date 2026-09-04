class bankAccount:
    __PINNumber = "2912"
    def __init__(self, BankCompany):
        self.BankCompany = BankCompany
info=bankAccount("Chase")
print(info.BankCompany)
print(info.__PINNumber)