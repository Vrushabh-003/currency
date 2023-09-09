from forex_python.converter import CurrencyRates
amount=float(input("Enter Amount to be Converted: "))
source_currency=input("Enter the source currency(eg: USD, INR, EUR) :").upper()
target_currency=input("Enter the target currency(eg: USD, INR, EUR) :").upper()
c=CurrencyRates()
converted_amount=c.convert(source_currency,target_currency,amount)
print(f"{amount} {source_currency} to {target_currency} is equal to :{converted_amount} {target_currency}")
